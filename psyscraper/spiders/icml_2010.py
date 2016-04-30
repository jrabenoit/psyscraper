import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider2010(scrapy.Spider):
    name = "icml_2010"
    allowed_domains = [
        'icml2010.org'
        ]
    start_urls = [
        'http://www.icml2010.org/abstracts.html'
        ]

    def parse(self, response): 
        sequence1 = range(1,8)
        iterator1 = sequence1.__iter__()
        iter_value1 = iterator1.next()        
        for iter_value1 in sequence1:       
            link_value1 = iter_value1 * 4
            for selection in response.xpath('//*[@id="Content"]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('table//table[1]//h3[%s]/text()'%(iter_value1)).extract()
                #item['link'] = selection.xpath('table//table[1]//p[%s]/a/@href'%(link_value1)).extract()
                #item['link'] = re.findall(r"'(.*?)'", '%s' % item['link'])
                #item['link'] = [u'http://www.icml2010.org/%s' % "".join(item['link'])]
                yield item
              
        sequence2 = range(8,153)
        iterator2 = sequence2.__iter__()
        iter_value2 = iterator2.next()        
        for iter_value2 in sequence2:       
            link_value2 = iter_value2 * 4
            for selection in response.xpath('//*[@id="Content"]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('table//table[2]//h3[%s]/text()'%(iter_value2)).extract()
                #item['link'] = selection.xpath('table//table[2]//p[%s]/a/@href'%(link_value2)).extract()
                #item['link'] = re.findall(r"'(.*?)'", '%s' % item['link'])
                #item['link'] = [u'http://www.icml2010.org/%s' % "".join(item['link'])]
                yield item  
         
