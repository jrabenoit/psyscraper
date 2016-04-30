import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "jair_2005_2014"
    allowed_domains = [
        'jair.org'
        ]
    #sequence1 = range(23,52)
    #iterator1 = sequence1.__iter__()
    #iter_value1 = iterator1.next() 
    #for iter_value1 in sequence1: 
    start_urls = [
            'http://www.jair.org/vol/vol23.html',
            'http://www.jair.org/vol/vol24.html',
            'http://www.jair.org/vol/vol25.html',
            'http://www.jair.org/vol/vol26.html',
            'http://www.jair.org/vol/vol27.html',
            'http://www.jair.org/vol/vol28.html',
            'http://www.jair.org/vol/vol29.html',
            'http://www.jair.org/vol/vol30.html',
            'http://www.jair.org/vol/vol31.html',
            'http://www.jair.org/vol/vol32.html',
            'http://www.jair.org/vol/vol33.html',
            'http://www.jair.org/vol/vol34.html',
            'http://www.jair.org/vol/vol35.html',
            'http://www.jair.org/vol/vol36.html',
            'http://www.jair.org/vol/vol37.html',
            'http://www.jair.org/vol/vol38.html',
            'http://www.jair.org/vol/vol39.html',
            'http://www.jair.org/vol/vol40.html',
            'http://www.jair.org/vol/vol41.html',
            'http://www.jair.org/vol/vol42.html',
            'http://www.jair.org/vol/vol43.html',
            'http://www.jair.org/vol/vol44.html',
            'http://www.jair.org/vol/vol45.html',
            'http://www.jair.org/vol/vol46.html',
            'http://www.jair.org/vol/vol47.html',
            'http://www.jair.org/vol/vol48.html',
            'http://www.jair.org/vol/vol49.html',
            'http://www.jair.org/vol/vol50.html',
            'http://www.jair.org/vol/vol51.html'
            ]
    def parse(self, response): 
        for selection in response.xpath('//*[@id="content"]/div/div'):                
            item = PsyscraperItem()
            item['title'] = selection.xpath('./meta[@name="citation_title"]/@content').extract()
            yield item
