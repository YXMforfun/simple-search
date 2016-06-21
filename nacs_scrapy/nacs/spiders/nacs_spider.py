import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from nacs.items import NacsItem

class nacsSpider(scrapy.Spider):
	name = "nacs"
	allow_domains = ["http://www.51nacs.com"]
	start_urls = [
			"http://www.51nacs.com/design/base/index.shtml",
			"http://www.51nacs.com/design/art/index.shtml",
			"http://www.51nacs.com/design/history/index.shtml",
			"http://www.51nacs.com/design/match/index.shtml",
			"http://www.51nacs.com/skill/pattern/index.shtml",
			"http://www.51nacs.com/skill/sew/index.shtml",
			"http://www.51nacs.com/skill/apparels/index.shtml",
			"http://www.51nacs.com/sl/es/index.shtml"
		]

	def parse(self, response):
		sel = Selector(response)
		urls = sel.xpath('//div[@class="list_nr"]//li//h2//@href').extract()
		for url in urls:
			yield Request(url, callback=self.parse_item)
		main = response.url[:response.url.rfind('/')]
		page = sel.xpath('//div[@class="page"]//@href').extract()
		next_page = main + page[-2][1:]
		final_page = main + page[-1][1:]
		if response.url != final_page:
			yield Request(next_page,callback=self.parse)

	def parse_item(self, response):
		item = NacsItem()
		sel = Selector(response)
		item['link'] = response.url
		item['title'] = sel.xpath('//div[@class="news_tit"]/text()').extract()
		data = sel.xpath('//div[@class="news_con"]')
		item['content'] = data.xpath('string(.)').extract()
		

		yield item
