# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidubaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = scrapy.Field()
    URL = scrapy.Field()
    Place = scrapy.Field()
    Title = scrapy.Field()
    Prefix = scrapy.Field()


class FileItem(scrapy.Item):
    Place = scrapy.Field()
    Content = scrapy.Field()