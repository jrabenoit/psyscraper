import scrapy
from scrapy.contrib.spiders import Rule

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "miccai_2005_2014"
    allowed_domains = [
        'springer.com'
        ]
    start_urls = [
        #links to Springer here --> http://www.miccai.org/PastProceedings
        #2005 part 1
        'http://link.springer.com/book/10.1007/11566465/page/1',
        'http://link.springer.com/book/10.1007/11566465/page/2',
        'http://link.springer.com/book/10.1007/11566465/page/3',
        'http://link.springer.com/book/10.1007/11566465/page/4',
        'http://link.springer.com/book/10.1007/11566465/page/5',
        'http://link.springer.com/book/10.1007/11566465/page/6',
        #2005 part 2
        'http://link.springer.com/book/10.1007/11566489/page/1',
        'http://link.springer.com/book/10.1007/11566489/page/2',
        'http://link.springer.com/book/10.1007/11566489/page/3',
        'http://link.springer.com/book/10.1007/11566489/page/4',
        'http://link.springer.com/book/10.1007/11566489/page/5',
        'http://link.springer.com/book/10.1007/11566489/page/6',
        'http://link.springer.com/book/10.1007/11566489/page/7',
        #2006 part 1
        'http://link.springer.com/book/10.1007/11866565/page/1',
        'http://link.springer.com/book/10.1007/11866565/page/2',
        'http://link.springer.com/book/10.1007/11866565/page/3',
        'http://link.springer.com/book/10.1007/11866565/page/4',
        'http://link.springer.com/book/10.1007/11866565/page/5',
        'http://link.springer.com/book/10.1007/11866565/page/6',
        #2006 part 2
        'http://link.springer.com/book/10.1007/11866763/page/1',
        'http://link.springer.com/book/10.1007/11866763/page/2',
        'http://link.springer.com/book/10.1007/11866763/page/3',
        'http://link.springer.com/book/10.1007/11866763/page/4',
        'http://link.springer.com/book/10.1007/11866763/page/5',
        'http://link.springer.com/book/10.1007/11866763/page/6',
        #2007 part 1
        'http://link.springer.com/book/10.1007/978-3-540-75757-3/page/1',
        'http://link.springer.com/book/10.1007/978-3-540-75757-3/page/2',
        'http://link.springer.com/book/10.1007/978-3-540-75757-3/page/3',
        'http://link.springer.com/book/10.1007/978-3-540-75757-3/page/4',
        'http://link.springer.com/book/10.1007/978-3-540-75757-3/page/5',
        'http://link.springer.com/book/10.1007/978-3-540-75757-3/page/6',
        #2007 part 2
        'http://link.springer.com/book/10.1007/978-3-540-75759-7/page/1',
        'http://link.springer.com/book/10.1007/978-3-540-75759-7/page/2',
        'http://link.springer.com/book/10.1007/978-3-540-75759-7/page/3',
        'http://link.springer.com/book/10.1007/978-3-540-75759-7/page/4',
        'http://link.springer.com/book/10.1007/978-3-540-75759-7/page/5',
        'http://link.springer.com/book/10.1007/978-3-540-75759-7/page/6',
        #2008 part 1
        'http://link.springer.com/book/10.1007/978-3-540-85988-8/page/1',
        'http://link.springer.com/book/10.1007/978-3-540-85988-8/page/2',
        'http://link.springer.com/book/10.1007/978-3-540-85988-8/page/3',
        'http://link.springer.com/book/10.1007/978-3-540-85988-8/page/4',
        'http://link.springer.com/book/10.1007/978-3-540-85988-8/page/5',
        'http://link.springer.com/book/10.1007/978-3-540-85988-8/page/6',
        'http://link.springer.com/book/10.1007/978-3-540-85988-8/page/7',
        #2008 part 2
        'http://link.springer.com/book/10.1007/978-3-540-85990-1/page/1',
        'http://link.springer.com/book/10.1007/978-3-540-85990-1/page/2',
        'http://link.springer.com/book/10.1007/978-3-540-85990-1/page/3',
        'http://link.springer.com/book/10.1007/978-3-540-85990-1/page/4',
        'http://link.springer.com/book/10.1007/978-3-540-85990-1/page/5',
        'http://link.springer.com/book/10.1007/978-3-540-85990-1/page/6',
        'http://link.springer.com/book/10.1007/978-3-540-85990-1/page/7',
        #2009 part 1
        'http://link.springer.com/book/10.1007/978-3-642-04268-3/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-04268-3/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-04268-3/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-04268-3/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-04268-3/page/5',
        'http://link.springer.com/book/10.1007/978-3-642-04268-3/page/6',
        'http://link.springer.com/book/10.1007/978-3-642-04268-3/page/7',
        #2009 part 2
        'http://link.springer.com/book/10.1007/978-3-642-04271-3/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-04271-3/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-04271-3/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-04271-3/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-04271-3/page/5',
        'http://link.springer.com/book/10.1007/978-3-642-04271-3/page/6',
        'http://link.springer.com/book/10.1007/978-3-642-04271-3/page/7',
        #2010 part 1
        'http://link.springer.com/book/10.1007/978-3-642-15705-9/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-15705-9/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-15705-9/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-15705-9/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-15705-9/page/5',
        #2010 part 2
        'http://link.springer.com/book/10.1007/978-3-642-15745-5/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-15745-5/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-15745-5/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-15745-5/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-15745-5/page/5',
        #2010 part 3
        'http://link.springer.com/book/10.1007/978-3-642-15711-0/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-15711-0/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-15711-0/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-15711-0/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-15711-0/page/5',
        #2011 part 1
        'http://link.springer.com/book/10.1007/978-3-642-23623-5/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-23623-5/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-23623-5/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-23623-5/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-23623-5/page/5',
        #2011 part 2
        'http://link.springer.com/book/10.1007/978-3-642-23629-7/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-23629-7/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-23629-7/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-23629-7/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-23629-7/page/5',        
        #2011 part 3
        'http://link.springer.com/book/10.1007/978-3-642-23626-6/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-23626-6/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-23626-6/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-23626-6/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-23626-6/page/5',
        #2012 part 1
        'http://link.springer.com/book/10.1007/978-3-642-33415-3/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-33415-3/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-33415-3/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-33415-3/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-33415-3/page/5',
        #2012 part 2
        'http://link.springer.com/book/10.1007/978-3-642-33418-4/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-33418-4/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-33418-4/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-33418-4/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-33418-4/page/5',
        #2012 part 3
        'http://link.springer.com/book/10.1007/978-3-642-33454-2/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-33454-2/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-33454-2/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-33454-2/page/4',
        #2013 part 1
        'http://link.springer.com/book/10.1007/978-3-642-40811-3/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-40811-3/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-40811-3/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-40811-3/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-40811-3/page/5',
        #2013 part 2
        'http://link.springer.com/book/10.1007/978-3-642-40763-5/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-40763-5/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-40763-5/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-40763-5/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-40763-5/page/5',
        #2013 part 3
        'http://link.springer.com/book/10.1007/978-3-642-40760-4/page/1',
        'http://link.springer.com/book/10.1007/978-3-642-40760-4/page/2',
        'http://link.springer.com/book/10.1007/978-3-642-40760-4/page/3',
        'http://link.springer.com/book/10.1007/978-3-642-40760-4/page/4',
        'http://link.springer.com/book/10.1007/978-3-642-40760-4/page/5',
        #2014 part 1
        'http://link.springer.com/book/10.1007/978-3-319-10404-1/page/1',
        'http://link.springer.com/book/10.1007/978-3-319-10404-1/page/2',
        'http://link.springer.com/book/10.1007/978-3-319-10404-1/page/3',
        'http://link.springer.com/book/10.1007/978-3-319-10404-1/page/4',
        'http://link.springer.com/book/10.1007/978-3-319-10404-1/page/5',
        #2014 part 2
        'http://link.springer.com/book/10.1007/978-3-319-10470-6/page/1',
        'http://link.springer.com/book/10.1007/978-3-319-10470-6/page/2',
        'http://link.springer.com/book/10.1007/978-3-319-10470-6/page/3',
        'http://link.springer.com/book/10.1007/978-3-319-10470-6/page/4',
        'http://link.springer.com/book/10.1007/978-3-319-10470-6/page/5',
        #2014 part 3
        'http://link.springer.com/book/10.1007/978-3-319-10443-0/page/1',
        'http://link.springer.com/book/10.1007/978-3-319-10443-0/page/2',
        'http://link.springer.com/book/10.1007/978-3-319-10443-0/page/3'
        ]

    def parse(self, response): 
            for selection in response.xpath('//*[@class="title"]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('a/text()').extract()
                yield item

