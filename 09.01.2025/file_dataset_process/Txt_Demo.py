import pandas as pd
df=pd.read_csv(r'/\dataset\SalesTransactions.txt',
               encoding='utf-8', dtype='unicode',
               sep='\t', low_memory=False
               )
print(df)