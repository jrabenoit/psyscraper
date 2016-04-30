import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider2013(scrapy.Spider):
    name = "icml_2013"
    allowed_domains = [
        'jmlr.org'
        ]
    start_urls = [
        'http://jmlr.org/proceedings/papers/v28/'
        ]

    def parse(self, response): 
        for selection in response.xpath('//*[@id="content"]/dl/div'):                
            item = PsyscraperItem()
            item['title'] = selection.xpath('p[1]/text()').extract()
            yield item
#//*[@id="content"]/dl[1]/div[1]/p[1]/text()

#//*[@id="content"]/dl[3]/div[167]/p[1]
