import scrapy
from scrapy.http import HtmlResponse
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ..items import DigItem

class DigSpider(CrawlSpider):
	name='spider'
	allowed_domains=['lishi.tianqi.com']
	start_urls=['http://lishi.tianqi.com/guilin/index.html']
	rules=(Rule(LinkExtractor(allow=r'http://lishi.tianqi.com/guilin/\d{6}.html'),callback='parse_item',follow=True),)

	def parse_item(self,response):
		item=DigItem()
		boxes=response.xpath('//div[@id="tool_site"]/div[@class="tqtongji2"]/ul[not(@class="t1")]')
		for box in boxes:
			a=box.xpath('.//li[1]/a/text()').extract() or box.xpath('.//li[1]/text()').extract()
			item['Date']=a
			item['Year']=a[0].split('-')[0]
			item['Month']=a[0].split('-')[1]
			item['Days']=a[0].split('-')[2]
			item['Temp_H']=box.xpath('.//li[2]/text()').extract()
			item['Temp_L']=box.xpath('.//li[3]/text()').extract()
			item['Dec']=box.xpath('li[4]/text()').extract()
			item['Wind']=box.xpath('li[5]/text()').extract()
			item['WindLevel']=box.xpath('li[6]/text()').extract()
			yield item