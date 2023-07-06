# -*- coding: utf-8 -*-
from os import path
import sqlite3
import scrapy
from urllib.parse import urlparse,unquote

from ..settings import EXPIRE_DAYS
from ..items import AhospitalItem

class HospitalSpider(scrapy.Spider):
    name = "HospitalSpider"
    start_urls = [
        'http://www.a-hospital.com/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95',
    ]
    restrict_hosts = set([urlparse(u).netloc for u in start_urls])
    db_conn:sqlite3.Connection = None 
    table_name = name.lower()

    def url_fetched(self, next_url) -> bool:
        return len(self.db_conn.execute(f"""select 1 from {self.table_name} where url = ? and
                                      created_at > datetime('now', '-{EXPIRE_DAYS} days')""", (next_url,)).fetchall()) > 1

    def parse(self, response):
        title = response.css("title::text").get().split()[0]
        paragraphs = response.css("div#bodyContent p,tr,li")
        next_pages = []
        page = []
        recently_updated = self.url_fetched(response.url)
        for r in paragraphs:
            if not recently_updated:
                if r.root.tag in {'tr', 'li'}:
                    if r.css("::text").getall() != r.css("a::text").getall():
                        page.append("".join([t.strip() for t in r.css("::text").getall()]))
                if r.root.tag == 'p':
                    page.append("".join(r.css("::text").getall()))
            
            next_pages += r.css("a::attr(href)").getall()
        
        # if the page was recently updated, dont update it again
        # but still we need to iterate over all of them to explore
        # the whole network
        if not recently_updated and len(page) > 0:
            yield AhospitalItem(url=response.url,
                title = title, paragragh='\n'.join(page))
        
        if len(next_pages) > 0:
            for n in next_pages:
                next_url = response.urljoin(n)
                up = urlparse(next_url)
                domain = up.netloc

                path_last = unquote(path.split(up.path)[-1].split(':')[0])
                if (domain in self.restrict_hosts and 
                     path_last != '用户') :
                    self.logger.info(f"forward to next url: {next_url}")
                    yield scrapy.Request(next_url)
                    return
                self.logger.info(f"skip url: {next_url}, domain: {domain}, path: {up.path}")
