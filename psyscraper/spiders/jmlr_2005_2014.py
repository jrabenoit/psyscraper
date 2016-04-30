import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "jmlr_2005_2014"
    allowed_domains = [
        'mit.edu'
        ]
    start_urls = [
        'http://jmlr.csail.mit.edu/papers/v6/',
        'http://jmlr.csail.mit.edu/papers/v7/',
        'http://jmlr.csail.mit.edu/papers/v8/',
        'http://jmlr.csail.mit.edu/papers/v9/',
        'http://jmlr.csail.mit.edu/papers/v10/',
        'http://jmlr.csail.mit.edu/papers/v11/',
        'http://jmlr.csail.mit.edu/papers/v12/',
        'http://jmlr.csail.mit.edu/papers/v13/',
        'http://jmlr.csail.mit.edu/papers/v14/',
        'http://jmlr.csail.mit.edu/papers/v15/',
        ]

    def parse(self, response): 
            for selection in response.xpath('//*[@id="content"]/dl/dt'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('./text()').extract()
                yield item

