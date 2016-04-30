import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "ijcai_2011"
    allowed_domains = [
        'ijcai.org'
        ]
    start_urls = [
        'http://ijcai.org/papers11/contents.php'
        ]

    def parse(self, response): 
        sequence1 = range(15,501)
        iterator1 = sequence1.__iter__()
        iter_value1 = iterator1.next()        
        for iter_value1 in sequence1: 
            for selection in response.xpath('/html/body/table[2]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('//p[%i]/a[1]/text()'%(iter_value1)).extract()
                yield item
                
                # Same odd problems as ijcai_2009.
