import itertools
import scrapy

from psyscraper.items import PsyscraperItem

class PsyscraperSpider2008(scrapy.Spider):
    name = "icml_2008"
    allowed_domains = [
        'machinelearning.org'
        ]
    start_urls = [
        'http://machinelearning.org/archive/icml2008/abstracts.shtml'
        ]

    def parse(self, response): 
        sequence = range(1,159)
        iterator = sequence.__iter__()
        iter_value = iterator.next()
        for iter_value in sequence:
            link_value = iter_value * 4
            for selection in response.xpath('/html/body/div/div[3]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('h3[%s]/text()'%(iter_value)).extract()
                #item['link'] = selection.xpath('p[%s]/a[1]/@href'%(link_value)).extract()
                yield item
