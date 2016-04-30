import scrapy
from psyscraper.items import PsyscraperItem


class PsyscraperSpider(scrapy.Spider):
    name = "icml_2005"
    allowed_domains = [
        'machinelearning.org'
        ]
    start_urls = [
        'http://machinelearning.org/icml2005_proc.html'
        ]

    def parse(self, response):
        for selection in response.xpath('//td'):
            item = PsyscraperItem()
            item['title'] = selection.xpath('a/text()').extract()
            #item['link'] = selection.xpath('a/@href').extract()
            yield item
