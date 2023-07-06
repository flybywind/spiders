# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AhospitalItem(scrapy.Item):
    def __init__(self, url, title, paragraph):
        self.fields['url'] = url 
        self.fields['title'] = title
        self.fields['paragragh'] = paragraph

    def __getattr__(self, name):
        if name in self.fields:
            return self.fields[name]
        else:
            return super().__getattr__(name)

    
