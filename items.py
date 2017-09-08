# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DigItem(scrapy.Item):
	Date=scrapy.Field()
	Month=scrapy.Field()
	Year=scrapy.Field()
	Days=scrapy.Field()
	Temp_H=scrapy.Field()
	Temp_L=scrapy.Field()
	Dec=scrapy.Field()
	Wind=scrapy.Field()
	WindLevel=scrapy.Field()
