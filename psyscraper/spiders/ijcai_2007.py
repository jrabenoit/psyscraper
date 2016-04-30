import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "ijcai_2007"
    allowed_domains = [
        'ijcai.org'
        ]
    start_urls = [
        'http://ijcai.org/Past%20Proceedings/IJCAI-2007/CONTENT/contents2007.html'
        ]

    def parse(self, response): 
        sequence1 = range(8,480)
        iterator1 = sequence1.__iter__()
        iter_value1 = iterator1.next()        
        for iter_value1 in sequence1: 
            for selection in response.xpath('/html/body/table[2]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('//p[%s]/a/text()'%(iter_value1)).extract()
                yield item
                
