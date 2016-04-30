import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider2009(scrapy.Spider):
    name = "icml_2009"
    allowed_domains = [
        'machinelearning.org'
        ]
    start_urls = [
        'http://machinelearning.org/archive/icml2009/abstracts.html'
        ]

    def parse(self, response): 
        # Sequence for first half of paper titles
        sequence1 = range(2,83)
        iterator1 = sequence1.__iter__()
        iter_value1 = iterator1.next()
        #Loop for first half of papers
        for iter_value1 in sequence1:       
            link_value1 = iter_value1 * 2 - 3
            for selection in response.xpath('//*[@id="right_column"]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('h3[%s]/text()'%(iter_value1)).extract()
                #item['link'] = selection.xpath('a[%s]/@href'%(link_value1)).extract()
                #item['link'] = re.findall(r"'(.*?)'", '%s' % item['link'])
                #item['link'] = [u'http://machinelearning.org/archive/icml2009/%s' % "".join(item['link'])]
                yield item
        #XPath naming scheme changed halfway through
        sequence2 = range(83,162)
        iterator2 = sequence2.__iter__()
        iter_value2 = iterator2.next()               
        for iter_value2 in sequence2:
            link_value2 = iter_value2 * 2 - 2      
            for selection in response.xpath('//*[@id="right_column"]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('h3[%s]/text()'%(iter_value2)).extract()
                #item['link'] = selection.xpath('a[%s]/@href'%(link_value2)).extract()
                #item['link'] = re.findall(r"'(.*?)'", '%s' % item['link'])
                #item['link'] = [u'http://machinelearning.org/archive/icml2009/%s' % "".join(item['link'])]
                yield item
