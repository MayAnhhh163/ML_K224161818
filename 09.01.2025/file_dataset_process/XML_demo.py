from bs4 import BeautifulSoup
with open(r'/\dataset\SalesTransactions.xml', 'r') as f:
    data = f.read()
bs_data = BeautifulSoup(data,'xml')

UelSample = bs_data.find_all('UelSample')
print(UelSample)

###đọc dữ liệu XML – Pandas XML

import pandas_read_xml as pdx
df = pdx.read_xml(r'D:\mhe\GitHub\ML_K224161818\dataset\SalesTransactions.xml',['UelSample','SalesItem'])
print(df)
print(df.iloc[0])
data=df.iloc[0]

print(data[0])
print(data[1])
print(data[1]['OrderID'])
