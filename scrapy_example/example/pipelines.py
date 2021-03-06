# -*- coding: utf-8 -*-
from pymongo import MongoClient
from scrapy.conf import settings
from scrapy import log
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ExamplePipeline(object):

    def __init__(self):
	client = MongoClient(settings['MONGODB_HOST'],settings['MONGODB_PORT'])
	db = client[settings['MONGODB_DB']]
	self.collection = db[settings['MONGODB_COLLECTION']]
    

    def process_item(self, item, spider):
	
	item_dict = dict(item)
	valid = True
	for data in item:
	    if not data:
		valid = False
		raise DropItem("Missing {0}".format(data))
	if valid:
	    self.collection.insert(item_dict)
	    log.msg("Index added to MongoDB database!",
		    level=log.DEBUG, spider=spider)
        return item
