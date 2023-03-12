import logging
import sqlite3
import scrapy
import pathlib

cur_dir = pathlib.Path(__file__).absolute().parent.parent

try:
    from conf import *
    from sqlite_pipeline import SqlitePipeline
    from sqlite_dao import SqliteDB
    from utils import get_url_from_href
except:
    raise RuntimeError("can't load internal packages")


class GushiwenSpider(scrapy.Spider):
    name = SPIDER_NAME
    start_urls = [
        'https://so.gushiwen.cn/gushi/sanbai.aspx',
    ]
    custom_settings = {
        'DB_PATH': cur_dir.joinpath("sqlite").as_posix(),
        'ITEM_PIPELINES': {
            SqlitePipeline: 900
        }
    }

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.db_dao = SqliteDB(
            GushiwenSpider.custom_settings.get("DB_PATH", "."))

    def parse(self, response, **kwargs):
        op = kwargs.get('op', "next")
        if op == "end":

            title = response.selector.css(".cont h1::text").get()
            poem = response.selector.css(".cont .contson")[0]
            poem = poem.css("::text").getall()
            poem_lines = self._clear_text(poem, POEM_THR)
            author = response.selector.css(
                ".cont p.source a::text")[:2].getall()

            yiwen = response.selector.css(".contyishang")[0]
            yiwen = yiwen.css("p::text").getall()[1:]
            yiwen_lines = self._clear_text(yiwen, YIWEN_THR)
            if len(poem_lines) > 0 and len(author) > 0:
                yield {
                    'title': title,
                    'url': response.url,
                    'author': "".join(author),
                    'poem': poem_lines,
                    'yiwen': yiwen_lines
                }
        elif op == "next":
            for next_page in response.selector.css(".left .typecont a::attr('href')"):
                next_url = get_url_from_href(
                    response.url, next_page.get())
                if self.db_dao.has_crawled(next_url, CRAWLER_REFRESH_DAYS):
                    logging.info(f"skip url: {next_url}")
                    return
                yield response.follow(next_page.get(), self.parse, cb_kwargs={'op': 'end'})
            for next_page in response.selector.css(".right .cont a::attr('href')"):
                next_url = get_url_from_href(
                    response.url, next_page.get())
                if self.db_dao.has_crawled(next_url, CRAWLER_REFRESH_DAYS):
                    logging.info(f"skip url: {next_url}")
                    return
                yield response.follow(next_page.get(), self.parse, cb_kwargs={'op': 'next'})

    def _clear_text(self, ll, thr=0):
        ll = [l.strip() for l in ll]
        return [l for l in ll if len(l) >= thr]
