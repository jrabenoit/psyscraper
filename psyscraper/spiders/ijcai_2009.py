import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "ijcai_2009"
    allowed_domains = [
        'ijcai.org'
        ]
    start_urls = [
        'http://ijcai.org/papers09/contents.php'
        ]

    def parse(self, response): 
        sequence1 = range(10,352)
        iterator1 = sequence1.__iter__()
        iter_value1 = iterator1.next()        
        for iter_value1 in sequence1: 
            for selection in response.xpath('/html/body/table[2]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('//p[%i]/a[2]/text()'%(iter_value1)).extract()
                print '%s'%(iter_value1)
                yield item
                
                # Few strange things happening here, but not enough to spend more time.
                # 1. XPath is not returning the correct count of /p[]/ tag- returning the one 7 later
                # 2. Some characters are unicode, e.g. /ufb01 == "f" but shows up in search results as /ufb01
                # 3. There are blank titles at the end of the search, even though the last paper is found properly.
                
