# -*- coding: utf-8 -*-
import scrapy

from ..items import AhospitalItem

class HospitalSpider(scrapy.Spider):
    name = "HospitalSpider"
    start_urls = [
        'http://www.a-hospital.com/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95',
    ]
    history_urls = set()

    def parse(self, response):
        title = response.css("title::text").get().split()[0]
        paragraphs = response.css("div#bodyContent p,tr,li")
        next_pages = []
        page = []
        for r in paragraphs:
            if r.root.tag in {'tr', 'li'}:
                next_pages += r.css("a::attr(href)").getall()
                if r.css("::text").getall() != r.css("a::text").getall():
                    page.append("".join([t.strip() for t in r.css("::text").getall()]))
            if r.root.tag == 'p':
                page.append("".join(r.css("::text").getall()))

            yield AhospitalItem(url=response.url,
                title = title, paragraph='\n'.join(page))

        if len(next_pages) > 0:
            for n in next_pages:
                next_url = response.urljoin(n)
                if next_url not in self.history_urls:
                    yield scrapy.Request(next_url)
