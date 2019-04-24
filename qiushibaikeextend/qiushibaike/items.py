# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class QItemLoader(ItemLoader):
    # //设置默认输出函数
    default_output_processor = TakeFirst()


class QiushibaikeItem(scrapy.Item):
    inp = {'input_processor': MapCompose(lambda s: s.replace('\n', '').strip())}
    name = scrapy.Field(inp)
    info = scrapy.Field(inp)
    crawl_date = scrapy.Field()
