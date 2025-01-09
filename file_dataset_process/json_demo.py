import pandas as pd
df=pd.read_json(r'D:\mhe\GitHub\ML_K224161818\dataset\SalesTransactions.json',
               encoding='utf-8',dtype='unicode'
               )
print(df)