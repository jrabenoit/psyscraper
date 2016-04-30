import itertools
import scrapy
import re

from psyscraper.items import PsyscraperItem

class PsyscraperSpider(scrapy.Spider):
    name = "uai_2005_2013"
    allowed_domains = [
        'dslpitt.org'
        ]
    start_urls = [
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=21',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=22',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=23',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=24',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=25',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=26',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=27',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=28',
        'https://dslpitt.org/uai/displayArticles.jsp?mmnu=1&smnu=1&proceeding_id=29',
        ]

    def parse(self, response): 
            for selection in response.xpath('//*[@class="cArticlesLstTitle"]'):                
                item = PsyscraperItem()
                item['title'] = selection.xpath('a/text()').extract()
                yield item

