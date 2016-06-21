# -*- coding: utf-8 -*-

# Scrapy settings for nacs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'nacs'

SPIDER_MODULES = ['nacs.spiders']
NEWSPIDER_MODULE = 'nacs.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nacs (+http://www.yourdomain.com)'

ITEM_PIPELINES = {"nacs.pipelines.NacsPipeline" : 1}

MONGODB_HOST = "localhost"
MONGODB_PORT =27017
MONGODB_DB = "examdb"
MONGODB_COLLECTION = "search"
