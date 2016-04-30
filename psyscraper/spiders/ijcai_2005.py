import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "ijcai_2005"
    allowed_domains = [
        'ijcai.org'
        ]
    start_urls = [
        'http://ijcai.org/Past%20Proceedings/IJCAI-05/IJCAI-05%20CONTENT.htm'
        ]

    def parse(self, response): 
        for selection in response.xpath('//*[@class="doctitle"]'):                
            item = PsyscraperItem()
            item['title'] = selection.xpath('a/text()').extract()
            yield item
            
