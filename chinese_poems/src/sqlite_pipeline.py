import logging
from os import path
import sqlite3

from conf import SPIDER_NAME


class SqlitePipeline:
    collection_name = SPIDER_NAME
    table_name = SPIDER_NAME

    def __init__(self, parent_dir="."):
        logging.info(f'db path = {parent_dir}')
        self.db_conn = sqlite3.connect(
            path.join(parent_dir, f"{SPIDER_NAME}.db"))
        self.cursor = self.db_conn.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        return SqlitePipeline(crawler.settings.get("DB_PATH", "."))

    def open_spider(self, spider):
        self.cursor.executescript(f'''
        BEGIN;
        CREATE TABLE if not exists {SqlitePipeline.table_name}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL UNIQUE,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                poem TEXT NOT NULL,
                yiwen TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
        CREATE INDEX if not exists url_index ON {SqlitePipeline.table_name} (url);
        CREATE INDEX if not exists title_index ON {SqlitePipeline.table_name} (title);
        CREATE INDEX if not exists author_index ON {SqlitePipeline.table_name} (author);
        COMMIT;
        ''')

    def close_spider(self, spider):
        self.db_conn.close()

    def process_item(self, item, spider):
        with self.db_conn:
            self.db_conn.execute(f'''INSERT OR REPLACE into {SqlitePipeline.table_name}(author, url, title, poem, yiwen, created_at) 
                                        VALUES(?, ?, ?, ?, ?, CURRENT_TIMESTAMP)''',
                                 (item.get("author"), item.get("url"), item.get("title"), "\n".join(item.get("poem")), "\n".join(item.get("yiwen")),))
        return item
