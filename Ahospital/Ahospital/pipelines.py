# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from os import path
import os
import sqlite3
import sys
import traceback
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from .settings import DB_PATH, EXPIRE_DAYS

class AhospitalPipeline:
    def open_spider(self, spider):
        spider.logger.info(f'openning spider with name: {spider.name}')
        if not path.exists(DB_PATH):
            os.mkdir(DB_PATH)
        self.db_conn = sqlite3.connect(path.join(DB_PATH, f"{spider.name}.db"))
        self.table_name = spider.name.lower()
        self.db_conn.executescript(f'''
        BEGIN;
        CREATE TABLE if not exists {self.table_name}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                paragragh TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
        CREATE INDEX if not exists url_index ON {self.table_name} (url);
        COMMIT;
        ''')
        spider.start_urls += [u[0] for u in self.db_conn.execute(
            f"select url from {self.table_name} where created_at > datetime('now', '-{EXPIRE_DAYS} days') order by created_at").fetchall()]
        spider.db_conn = self.db_conn
        spider.logger.info(f'start from {len(spider.start_urls)} init urls')


    def close_spider(self, spider):
        self.db_conn.close()

    def process_item(self, item, spider):
        try:
            with self.db_conn:
                self.db_conn.execute(f'''INSERT OR REPLACE into {self.table_name} (url, title, paragragh, created_at) 
                                            VALUES(?, ?, ?, CURRENT_TIMESTAMP)''',
                                    (item.get("url"), 
                                    item.get("title"), 
                                    item.get("paragragh"),))
            return {"text": item.get('paragragh')}
        except:
            traceback.print_exc()
            sys.exit(-1)
