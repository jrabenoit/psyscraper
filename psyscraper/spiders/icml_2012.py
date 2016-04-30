import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider2012(scrapy.Spider):
    name = "icml_2012"
    allowed_domains = [
        'icml.cc'
        ]
    start_urls = [
        'http://icml.cc/2012/papers/'
        ]

    def parse(self, response): 
        for selection in response.xpath('//*[@id="content"]/div'):                
            item = PsyscraperItem()
            item['title'] = selection.xpath('h2/text()').extract()
            yield item

