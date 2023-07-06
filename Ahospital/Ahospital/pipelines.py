# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from os import path
import os
import sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AhospitalPipeline:
    def open_spider(self, spider):
        db_path = spider.custom_settings.get("DB_PATH")
        if not path.exists(db_path):
            os.mkdir(db_path)
        self.expire_days = spider.custom_settings.get("EXPIRE_DAYS", 30)
        self.db_conn = sqlite3.connect(path.join(db_path, f"{spider.name}.db"))
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
        spider.history_urls = set(
            self.cursor.execute(f"select url from ? where create_at > datetime('now', '-{self.expire_days} days') order by create_at", self.table_name)
            .fetchall())
        spider.logger.info(f"open sqlite success with table {self.table_name}, hisotry url len = {len(spider.history_urls)}")
        if len(spider.history_urls) > 0:
            spider.logger.info(f"earlist 5 urls:\n{spider.history_urls[:5]}")

    def process_item(self, item, spider):
        self.db_conn.execute(f'''INSERT OR REPLACE into ? (url, title, paragragh, created_at) 
                                        VALUES(?, ?, ?, CURRENT_TIMESTAMP)''',
                                 (self.table_name, 
                                  item.get("url"), 
                                  item.get("title"), 
                                  item.get("paragragh"),))
        spider.history_urls.add(item.url)
        return item.paragragh
