import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "mlj_2005_2014"
    allowed_domains = [
        'springer.com'
        ]

    start_urls_list = []
    sequence1 = [
        "58/1", "58/2", "59/1", "59/3", "60/1", "61/1", "62/1", "62/3", "63/1", "63/2", "63/3", "64/1", "65/1", "65/2", "66/1", "66/2", "67/1", "67/3", "68/1", "68/2", "68/3", "69/1", "69/2", "70/1", "70/2", "71/1", "71/2", "72/1", "72/3", "73/1", "73/2", "73/3", "74/1", "74/2", "74/3", "75/1", "75/2", "75/3", "76/1", "76/2", "77/1", "77/2", "78/1", "78/3", "79/1", "79/3", "80/1", "80/2", "81/1", "81/2", "81/3", "82/1", "82/2", "82/3", "83/1", "83/2", "83/3", "84/1", "84/3", "85/1", "85/3", "86/1", "86/2", "86/3", "87/1", "87/2", "87/3", "88/1", "88/3", "89/1", "89/3", "90/1", "90/2", "90/3", "91/1", "91/2", "91/3", "92/1", "92/2", "93/1", "93/2", "94/1", "94/2", "94/3", "95/1", "95/2", "95/3", "96/1", "96/3", "97/1", "97/3"
        ]
#This is a neat little iterator that reduces the need for endless copypasta, enabling creation of the list of start_urls from, for example, a text file outside the program.
    iterator1 = sequence1.__iter__()
    iter_value1 = iterator1.next() 
    
    for iter_value1 in sequence1: 
        iter_url='http://link.springer.com/journal/10994/%s'%(iter_value1)
        start_urls_list.append(iter_url)
    
    start_urls = start_urls_list

    def parse(self, response): 
            for selection in response.xpath('//h3[contains(@class,"title")]'): # Springer likes to use an "embed" tag for papers that reference other papers in their title. I'm going to ignore this for now, but may revisit later if we find many partial or cut-off titles.
                item = PsyscraperItem()
                item['title'] = selection.xpath('.//a/text()').extract()
                yield item
           
