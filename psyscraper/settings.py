# -*- coding: utf-8 -*-

# Scrapy settings for psyscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'psyscraper'

SPIDER_MODULES = ['psyscraper.spiders']
NEWSPIDER_MODULE = 'psyscraper.spiders'

ITEM_PIPELINES = {'psyscraper.pipelines.PsyscraperPipeline': 100}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'psyscraper (+http://www.yourdomain.com)'
