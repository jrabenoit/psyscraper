import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider2014(scrapy.Spider):
    name = "icml_2014"
    allowed_domains = [
        'jmlr.org'
        ]
    start_urls = [
        'http://jmlr.org/proceedings/papers/v32/'
        ]

    def parse(self, response): 
        for selection in response.xpath('//*[@id="content"]/dl/div'):                
            item = PsyscraperItem()
            item['title'] = selection.xpath('p[1]/text()').extract()
            yield item
