import scrapy
from psyscraper.items import PsyscraperItem


class PsyscraperSpider(scrapy.Spider):
    name = "icml_2006"
    allowed_domains = [
        'machinelearning.org'
        ]
    start_urls = [
        'http://machinelearning.org/icml2006_proc.html'
        ]

    def parse(self, response):
        for selection in response.xpath('//sub'):
            item = PsyscraperItem()
            item['title'] = selection.xpath('a/em/text()').extract()
            item['link'] = selection.xpath('a/@href').extract()
            yield item
