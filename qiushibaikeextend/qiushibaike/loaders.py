# -*- coding: utf-8 -*-
# @Time : 2018/11/5 10:44 AM
# @Author : cxa
# @File : loaders.py
# @Software: PyCharm

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose


class Loader(ItemLoader):
    default_output_processor = TakeFirst()

