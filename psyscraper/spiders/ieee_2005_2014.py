# There is no easy way to search all IEEE articles except by using their Xplore digital library. This is because IEEE is divided up into numerous conferences and journals and workshops, any number of which might contain relevant articles. So we're doing this the hard way and using the digital library, and all 3210 pages of results.

# Query used: ("machine learning" OR "SVM" OR "support vector machine" OR "classification" OR "neural network" OR "decision tree" OR "Bayesian network" OR "reinforcement learning" OR "sparse learning" OR "MVPA" OR "multivoxel pattern analysis" OR "automated diagnosis" OR "computerized diagnosis")

import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "ieee_2005_2014"
    allowed_domains = [
        'ieee.org'
        ]

    start_urls_list = []
    sequence1 = range(1, 3211)
    iterator1 = sequence1.__iter__()
    iter_value1 = iterator1.next() 
    
    for iter_value1 in sequence1: 
        iter_url='http://ieeexplore.ieee.org/search/searchresult.jsp?ranges%%3D2005_2015_p_Publication_Year%%26matchBoolean%%3Dtrue%%26pageNumber%%3D2%%26rowsPerPage%%3D100%%26searchField%%3DSearch_All_Text%%26queryText%%3D%%28%%22machine+learning%%22+OR+%%0A%%22SVM%%22+OR%%0A%%22support+vector+machine%%22+OR%%0A%%22classification%%22+OR%%0A%%22neural+network%%22+OR%%0A%%22decision+tree%%22+OR%%0A%%22Bayesian+network%%22+OR%%0A%%22reinforcement+learning%%22+OR%%0A%%22sparse+learning%%22+OR%%0A%%22MVPA%%22+OR%%0A%%22multivoxel+pattern+analysis%%22+OR%%0A%%22automated+diagnosis%%22+OR%%0A%%22computerized+diagnosis%%22%%0A%%0A%%29&pageNumber=%s'%(iter_value1)
        start_urls_list.append(iter_url)
    
    start_urls = start_urls_list

# To my great fucking joy, there's a new problem. The problem is that the class is changed to "snippet" rather than "detail" whenever a keyword pops up, so we need a way of remaking the title into something useful. 
   
    def parse(self, response): 
            for selection in response.xpath('//*[@class="detail"]'):
                item = PsyscraperItem()
                item['title'] = selection.xpath('h3/a//text()').extract()
                #tem['link'] = selection.xpath('h3/a/@href').extract()
                yield item
                
                
                
