import pymssql
db=pymssql.connect(host='localhost',user='sa',password='xxxxxxx',database='Test',charset="utf8")
print(db)
cur=db.cursor()

sql='''CREATE TABLE WeatherRecord(
ID INT PRIMARY KEY IDENTITY,
DATE VARCHAR(255) NOT NULL,
YEAR INT NOT NULL,
MONTH INT NOT NULL,
DAYS INT NOT NULL,
TEMP_H INT NOT NULL,
TEMP_L INT NOT NULL,
WIND VARCHAR(255) NOT NULL,
WindLevel VARCHAR(255) NOT NULL,
DEC NVARCHAR(255) NOT NULL);'''
cur.execute(sql)
print("表格创建成功")
db.commit()
