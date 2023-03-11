import scrapy
from scrapy.http import HtmlResponse


class QuotesSpider(scrapy.Spider):
    name = 'chinese_poems'
    start_urls = [
        'https://so.gushiwen.cn/gushi/sanbai.aspx',
    ]

    def parse(self, response: HtmlResponse, kwargs: dict):
        op = kwargs['op']
        if op == "end":
            title = response.selector.css(".cont h1::text").get()
            poem = response.selector.css(
                ".cont .contson::text").getall()
            poem_lines = self._clear_text(poem)
            yiwen = response.selector.css(".contyishang")
            yiwen = yiwen.css("p::text").getall()
            yiwen_lines = self._clear_text(yiwen)
            if len(poem_lines) > 0 and len(yiwen_lines) > 0:
                yield {
                    'title': title,
                    'poem': poem_lines,
                    'yiwen': yiwen_lines
                }
        elif op == "next":
            for next_page in response.selector.css(".left .typecont a::attr('href')"):
                yield response.follow(next_page.get(), self.parse, cb_kwargs={'op': 'end'})
            for next_page in response.selector.css(".right .cont a::attr('href')"):
                yield response.follow(next_page.get(), self.parse, cb_kwargs={'op': 'next'})

    def _clear_text(ll):
        ll = [l.strip() for l in ll]
        return [l for l in ll if len(l) > 0]
