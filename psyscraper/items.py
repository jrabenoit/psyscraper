# -*- coding: utf-8 -*-

import scrapy

class PsyscraperItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    pass
