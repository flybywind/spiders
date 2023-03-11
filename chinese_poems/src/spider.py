import scrapy
from .conf import *
from .sqlite_pipeline import SqlitePipeline


class GushiwenSpider(scrapy.Spider):
    name = SPIDER_NAME
    start_urls = [
        'https://so.gushiwen.cn/gushi/sanbai.aspx',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            SqlitePipeline: 900
        }
    }

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
                    'author': "".join(author),
                    'poem': poem_lines,
                    'yiwen': yiwen_lines
                }
        elif op == "next":
            for next_page in response.selector.css(".left .typecont a::attr('href')"):
                yield response.follow(next_page.get(), self.parse, cb_kwargs={'op': 'end'})
            for next_page in response.selector.css(".right .cont a::attr('href')"):
                yield response.follow(next_page.get(), self.parse, cb_kwargs={'op': 'next'})

    def _clear_text(self, ll, thr=0):
        ll = [l.strip() for l in ll]
        return [l for l in ll if len(l) >= thr]
