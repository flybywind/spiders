# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AhospitalItem(scrapy.Item):
    url = scrapy.Field()
    title= scrapy.Field()
    paragragh = scrapy.Field()

    
