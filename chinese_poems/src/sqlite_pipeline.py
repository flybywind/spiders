from os import path
import sqlite3
from itemadapter import ItemAdapter

from .conf import SPIDER_NAME


class SqlitePipeline:
    collection_name = SPIDER_NAME
    table_name = SPIDER_NAME

    def __init__(self, parent_dir="."):
        self.db_conn = sqlite3.connect(
            path.join(parent_dir, f"{SqlitePipeline.collection_name}.db"))
        self.cursor = self.db_conn.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        print("create SqlitePipeline", crawler.settings.get('ITEM_PIPELINES'))

    def open_spider(self, spider):
        self.cursor.executescript(f'''
        BEGIN;
        CREATE TABLE if not exists {SqlitePipeline.table_name}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                poem TEXT NOT NULL,
                yiwen TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
        CREATE INDEX if not exists title_index ON {SqlitePipeline.table_name} (title);
        CREATE INDEX if not exists author_index ON {SqlitePipeline.table_name} (author);
        COMMIT;
        ''')

    def close_spider(self, spider):
        self.db_conn.close()

    def process_item(self, item, spider):
        with self.db_conn:
            self.db_conn.execute(f'''INSERT OR IGNORE into {SqlitePipeline.table_name}(author, title, poem, yiwen) 
                                        SELECT ?, ?, ?, ? WHERE NOT EXISTS 
                                            (SELECT * FROM {SqlitePipeline.table_name} WHERE author = ? and title = ?); ''',
                                 (item.get("author"), item.get("title"), "\n".join(item.get("poem")), "\n".join(item.get("yiwen")),
                                  item.get("author"), item.get("title")))
        return item
