import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "nips_2005_2013"
    allowed_domains = [
        'nips.cc'
        ]
    start_urls = [
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-18-2005',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-19-2006',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-20-2007',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-21-2008',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-22-2009',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-23-2010',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-24-2011',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-25-2012',
        'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-26-2013'
        ]
#should scrape 2466 items
    def parse(self, response): 
            for selection in response.xpath('/html/body/div[2]/div/ul/li/a[1]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('./text()').extract()
                yield item

