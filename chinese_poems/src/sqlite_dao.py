import sqlite3
from os import path

from conf import SPIDER_NAME

from typing import NamedTuple


class Row(NamedTuple):
    url: str
    author: str
    title: str
    poem: str
    yiwen: str

    @staticmethod
    def fields():
        return Row._fields


class SqliteDB():
    table_name = SPIDER_NAME

    def __init__(self, db_path) -> None:
        self.db_conn = sqlite3.connect(path.join(db_path, f"{SPIDER_NAME}.db"))

    def has_exist(self, url, title, author):
        r = self.db_conn.execute(f"SELECT 1 from {self.table_name} where url = ? and author = ? and title = ?",
                                 (url, author, title)
                                 ).fetchall()
        return len(r) > 0

    def has_crawled(self, url, dur=0):
        '''
          has crawled within recent `dur`` days
          '''
        r = self.db_conn.execute(f"SELECT 1 from {self.table_name} where url = ? and created_at > datetime('now', '-{dur} days')",
                                 (url, )
                                 ).fetchall()
        return len(r) > 0

    def scan_db(self, cond_sql):
        fields = Row.fields()
        select_sql = f"""SELECT {",".join(fields)} from {SqliteDB.table_name} where {cond_sql}"""
        result = self.db_conn.execute(select_sql)
        ret = []
        for r in result:
            dict_row = dict(zip(fields, r))
            ret.append(Row(**dict_row))
        return ret
