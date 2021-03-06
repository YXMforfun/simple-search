# -*- coding: utf-8 -*-


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml  import SgmlLinkExtractor
from example.items import ExampleItem

class ExampleSpider(scrapy.Spider):
	name = "example"
	allow_domains = ["www.fzengine.com"]
	start_urls = [
		"http://www.fzengine.com/kbase/KBclass_2.aspx",
		"http://www.fzengine.com/kbase/KBclass_3.aspx",
		"http://www.fzengine.com/kbase/KBclass_4.aspx",
		"http://www.fzengine.com/kbase/KBclass_5.aspx",
		"http://www.fzengine.com/kbase/KBclass_6.aspx",
		"http://www.fzengine.com/kbase/KBclass_7.aspx",
		"http://www.fzengine.com/kbase/KBclass_8.aspx",
		"http://www.fzengine.com/kbase/KBclass_9.aspx",
		"http://www.fzengine.com/kbase/KBclass_10.aspx",
		"http://www.fzengine.com/kbase/KBclass_11.aspx",
		"http://www.fzengine.com/kbase/KBclass_12.aspx",
		"http://www.fzengine.com/kbase/KBclass_13.aspx",
		"http://www.fzengine.com/kbase/KBclass_14.aspx",
		"http://www.fzengine.com/kbase/KBclass_15.aspx"
	]

	
	def parse(self,response):
		sel = Selector(response)
		urls = sel.xpath('//ul[@class="newlist"]//li//@href').extract()
		for url in urls:
			yield Request(url,callback=self.parse_item)
		page = sel.xpath('//div[@class="page"]//@href').extract()
		next_page = 'http://www.fzengine.com/kbase/'+ page[-2]
		final_page = 'http://www.fzengine.com/kbase/' + page[-1]
		if response.url != final_page:
			yield Request(next_page,callback=self.parse)
		

	def parse_item(self, response):
		item = ExampleItem()
		sel = Selector(response)
		item['link'] = response.url
		item['title'] = sel.xpath('//div[@class="showtitle"]/h1/text()').extract()
		data = sel.xpath('//div[@class="content"]')
		item['content'] = data.xpath('string(.)').extract()
		yield item
