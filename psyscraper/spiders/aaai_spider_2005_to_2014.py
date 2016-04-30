import scrapy
from psyscraper.items import PsyscraperItem


class PsyscraperSpider(scrapy.Spider):
    name = "aaai_2005_2014"
    allowed_domains = ["aaai.org"]
    start_urls = [
        #grabbing last 10 years of AAAI papers
        "http://www.aaai.org/Library/AAAI/aaai14contents.php",
        "http://www.aaai.org/Library/AAAI/aaai13contents.php",
        "http://www.aaai.org/Library/AAAI/aaai12contents.php",
        "http://www.aaai.org/Library/AAAI/aaai11contents.php",
        "http://www.aaai.org/Library/AAAI/aaai10contents.php",
        #There is no aaai 2009
        "http://www.aaai.org/Library/AAAI/aaai08contents.php",
        "http://www.aaai.org/Library/AAAI/aaai07contents.php",
        "http://www.aaai.org/Library/AAAI/aaai06contents.php",
        "http://www.aaai.org/Library/AAAI/aaai05contents.php"
    ]

    def parse(self, response):
        for selection in response.xpath('//*[@id="box6"]/div/p'):
            item = PsyscraperItem()
            item['title'] = selection.xpath('a/text()').extract()
            #item['link'] = selection.xpath('a/@href').extract()
            yield item

