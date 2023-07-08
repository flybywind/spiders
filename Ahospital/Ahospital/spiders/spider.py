# -*- coding: utf-8 -*-
from os import path
import sqlite3
import scrapy
from urllib.parse import urlparse,unquote

from ..settings import EXPIRE_DAYS
from ..items import AhospitalItem

END_ID = set(['fromlink', 'footer'])
class HospitalSpider(scrapy.Spider):
    name = "HospitalSpider"
    start_urls = [
        'http://www.a-hospital.com/w/%E6%80%8E%E6%A0%B7%E7%9C%8B%E5%8C%96%E9%AA%8C%E5%8D%95',
    ]
    restrict_hosts = set([urlparse(u).netloc for u in start_urls])
    db_conn:sqlite3.Connection = None 
    table_name = name.lower()

    def url_fetched(self, next_url) -> bool:
        return False if self.db_conn is None else \
              len(self.db_conn.execute(f"""select 1 from {self.table_name} where url = ? and
                                      created_at > datetime('now', '-{EXPIRE_DAYS} days')""", (next_url,)).fetchall()) > 1

    def parse(self, response):
        title = response.css("title::text").get().split()[0]
        paragraphs = response.css("div#bodyContent p,tr,li,div#fromlink,div#footer")
        nav_text = response.css(".nav ::text").getall()
        for nav in nav_text[1:]:
            if nav.find('制药企业列表') >= 0:
                self.logger.warning("skip company info page")
                return

        next_pages = []
        page = []
        recently_updated = self.url_fetched(response.url)
        for r in paragraphs:
            if r.root.attrib.get('id', "") in END_ID:
                break
            if not recently_updated:
                parent_text = [e for t in r.css("::text").getall() if len(e:=t.strip()) > 1]
                children_text = {e for t in r.css("a::text, a>*::text").getall() if len(e:=t.strip()) > 1}
                remain_text = "".join([e for e in parent_text if e not in children_text])
                if r.root.tag == 'tr':
                    parent_text = "\t".join(parent_text)
                else:
                    parent_text = "".join(e for e in r.css("::text").getall())
                if len(parent_text) > 0 \
                    and len(remain_text) / len(parent_text) > 0.2:
                    page.append(parent_text)
              
            next_pages += r.css("a::attr(href)").getall()
        
        # if the page was recently updated, dont update it again
        # but still we need to iterate over all of them to explore
        # the whole network
        if not recently_updated and len(page) > 4:
            average_sentence_len = sum(len(a) for a in page)/len(page)
            if  average_sentence_len > 20:
                yield AhospitalItem(url=response.url,
                    title = title, paragragh='\n'.join(page))
            else:
                self.logger.warning(f"skip page since the average setence length are too few: {response.url}")
        else:
            if recently_updated:
                self.logger.warning(f"skip page recently crawled {response.url}")
            else:
                self.logger.warning(f"skip page since the paragraghs are too few: {response.url}")
        
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
                else:
                    self.logger.warning(f"skip url: {next_url}, domain: {domain}, path: {up.path}")
        else:
            self.logger.info(f"no forward urls found in {response.url}")
