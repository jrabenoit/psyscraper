import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "aij_2005_2014"
    allowed_domains = [
        'sciencedirect.com'
        ]

    start_urls_list = []
    sequence1 = [
        "161/1-2", "162/1-2", "163/1", "163/2", "164/1-2", "165/1", "165/2", "166/1-2", "167/1-2", "168/1-2", "169/1", "169/2", "170/1", "170/2", "170/3", "170/4-5", "170/6-7", "170/8-9", "170/10", "170/11", "170/12-13", "170/14-15", "170-16-17", "170/18", "171/1", "171/2-3", "171/4", "171/5-6", "171/7", "171/8-9", "171/10-15", "171/16-17", "171/18", "172/1", "172/2-3", "172/4-5", "172/6-7", "172/8-9", "172/10", "172/11", "172/12-13", "172/14", "172/15", "172/16-17", "172/18", "173/1", "173/2", "173/3-4", "173/5-6", "173/7-8", "173/9-10", "173/11", "173/12-13", "173/14", "173/15", "173/16-17", "173/18", "174/1", "174/2", "174/3-4", "174/5-6", "174/7-8", "174/9-10", "174/11", "174/12-13", "174/14", "174/15", "174/16-17", "174/18", "175/1", "175/2", "175/3-4", "175/5-6", "175/7-8", "175/9-10", "175/11", "175/12-13", "175/14-15", "175/16-17", "175/18", "176/1", "177-179", "180-181", "182-183", "184-185", "186", "187-188", "189", "190", "191-192", "193", "194", "195", "196", "197", "198", "199-200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219"
        ]
#This is a neat little iterator that reduces the need for endless copypasta, enabling creation of the list of start_urls from, for example, a text file outside the program.
    iterator1 = sequence1.__iter__()
    iter_value1 = iterator1.next() 
    
    for iter_value1 in sequence1: 
        iter_url='http://www.sciencedirect.com/science/journal/00043702/%s'%(iter_value1)
        start_urls_list.append(iter_url)
    
    start_urls = start_urls_list

    def parse(self, response): 
            for selection in response.xpath('//li[contains(@class,"title")]'): # using contains because the Elsevier decided to switch their attribute names halfway through. This expression generalizes the class to any li's class attribute containing "title".            
                item = PsyscraperItem()
                item['title'] = selection.xpath('.//a/text()').extract()
                yield item
           
