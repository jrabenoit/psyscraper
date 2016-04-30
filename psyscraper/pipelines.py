#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

import json

class PsyscraperPipeline(object):

    def process_item(self, item, spider):
        
        with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_list', 'rb') as f:
            list1 = map(str.strip, f)
        #with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_list_lower', 'rb') as g:
            #list2 = map(str.strip, g)
        
        psyci_keywords= list1 #+list2

        # The following method works. Any() is efficient sugar syntax that short circuits searches upon finding a keyword match. str(item) is needed because it doesn't pull the item from file in a readable format without it.
        
        if any(x in str(item) for x in psyci_keywords):
            return item
        else:
            raise DropItem()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
