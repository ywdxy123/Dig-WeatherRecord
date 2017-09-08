import pymssql

class DigPipeline(object):
	def __init__(self):
		self.db=pymssql.connect(host='localhost',user='sa',password='ywdxy123',database='Test',charset="utf8")
		self.cur=self.db.cursor()

	def process_item(self, item, spider):
		
		sql="INSERT INTO WeatherH (DATE,TEMP_H,TEMP_L,WIND,WindLevel,DEC)"
		sql+="values('%s','%s','%s','%s','%s','%s');"%(item['Date'][0],item['Temp_H'][0],item['Temp_L'][0],item['Wind'][0],item['WindLevel'][0],item['Dec'][0])
		self.cur.execute(sql)
		self.db.commit()
		
		return item

		# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class DigPipeline(object):
	def __init__(self):
		self.file=codecs.open('Weather.json','w')
	def process_item(self, item, spider):
		line=json.dumps(dict(item))+'\n'
		self.file.write(line)
		return item

