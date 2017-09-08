import pymssql

class DigPipeline(object):
	def __init__(self):
		self.db=pymssql.connect(host='localhost',user='sa',password='XXXXXX',database='Test',charset="utf8")
		self.cur=self.db.cursor()

	def process_item(self, item, spider):
		
		sql="INSERT INTO WeatherRecord (DATE,YEAR,MONTH,DAYS,TEMP_H,TEMP_L,WIND,WindLevel,DEC)"
		sql+="values('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(item['Date'][0],item['Year'],item['Month'],item['Days'],item['Temp_H'][0],item['Temp_L'][0],item['Wind'][0],item['WindLevel'][0],item['Dec'][0])
		self.cur.execute(sql)
		self.db.commit()
		
		return item
