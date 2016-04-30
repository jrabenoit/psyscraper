import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider2011(scrapy.Spider):
    name = "icml_2011"
    allowed_domains = [
        'icml-2011.org'
        ]
    start_urls = [
        'http://www.icml-2011.org/papers.php'
        ]

    def parse(self, response): 
        sequence1 = range(9,161)
        iterator1 = sequence1.__iter__()
        iter_value1 = iterator1.next()        
        for iter_value1 in sequence1:       
            link_value1 = iter_value1
            for selection in response.xpath('//*[@style="width:900px"]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('tr[1]/td[2]/a[%s]/h3/text()'%(iter_value1)).extract()
                # Due to time constraints I'm pulling a plug on finding links.
                # Revisit when able, but low priority.
                #item['link'] = selection.xpath('p[%s]/a[2]/@href'%(link_value1)).extract()
                #item['link'] = re.findall(r'\"(.*?)\"', '%s' % item['link'])
                #item['link'] = [u'http://www.icml-2011.org/%s' % "".join(item['link'])]
                yield item
              

