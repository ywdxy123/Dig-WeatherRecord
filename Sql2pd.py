import numpy as np
import pandas as pd
import pymssql 
import matplotlib.pyplot as plt
select_sql='SELECT Date,TEMP_H,TEMP_L,Days,Month FROM WeatherRecord'
db=pymssql.connect(host='localhost',user='sa',password='xxxxxxx',database='Test',charset='utf8')
cur=db.cursor()

cur.execute(select_sql)
df=pd.read_sql(select_sql,db)

a=pd.DataFrame(df)
print(a)
