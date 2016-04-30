import scrapy
from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "icml_2007"
    allowed_domains = [
        'machinelearning.org'
        ]
    start_urls = [
        'http://machinelearning.org/icml2007_proc.html'
        ]

    def parse(self, response):
        for selection in response.xpath('//*[@id="icml-2007-proceedings"]/div'):
            item = PsyscraperItem()
            item['title'] = selection.xpath('h2/text()').extract()
            #item['link'] = selection.xpath('p/a[2]/@href').extract()
            yield item
           
