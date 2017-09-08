import pymssql
db=pymssql.connect(host='localhost',user='sa',password='ywdxy123',database='Test',charset="utf8")
print(db)
cur=db.cursor()

sql='''CREATE TABLE WeatherRecord(
ID INT PRIMARY KEY IDENTITY,
DATE VARCHAR(255) NOT NULL,
YEAR VARCHAR(255) NOT NULL,
MONTH VARCHAR(255) NOT NULL,
DAYS VARCHAR(255) NOT NULL,
TEMP_H VARCHAR(255) NOT NULL,
TEMP_L VARCHAR(255) NOT NULL,
WIND VARCHAR(255) NOT NULL,
WindLevel VARCHAR(255) NOT NULL,
DEC NVARCHAR(255) NOT NULL);'''
cur.execute(sql)
print("表格创建成功")
db.commit()
