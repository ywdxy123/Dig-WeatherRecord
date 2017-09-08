import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymssql 
select_sql='SELECT Date,TEMP_H,TEMP_L,Days,Month FROM WeatherRecord order by Date'
db=pymssql.connect(host='localhost',user='sa',password='xxxxxxx',database='Test',charset='utf8')
cur=db.cursor()

cur.execute(select_sql)
df=pd.read_sql(select_sql,db)

a=pd.DataFrame(df)
print(a)
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d %H:%M:%S')
a_Date=a.set_index('Date')
a_Date['TEMP_L'].plot()
plt.show()
