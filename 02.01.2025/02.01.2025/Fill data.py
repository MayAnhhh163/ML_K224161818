#Điền dữ liệu còn thiếu
from numpy import nan as NA
import numpy as np
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)

cleaned1 = data.fillna(0)
print(cleaned1)
print("-"*10)

cleaned2 = data.fillna(data.mean())
print(cleaned2)
print("-"*10)

cleaned3 = data.fillna(data.median())
print(cleaned3)
print("-"*10)

cleaned4 = data.fillna(data.mode().iloc[0])
print(cleaned4)
print("-"*10)

cleaned5 = data.ffill()
print(cleaned5)
print("-"*10)

cleaned6 = data.bfill()
print(cleaned6)
print("-"*10)

cleaned7 = data.interpolate(method='linear')
print(cleaned7)
print("-"*10)

data_filled = data.fillna(0)
cleaned8 = data_filled.interpolate(method='polynomial', order=2)
print(cleaned8)
print("-"*10)

cleaned9 = data.fillna({0: 0, 1: 99, 2: -1})
print(cleaned9)
print("-"*10)

cleaned10 = data.apply(lambda col: col.fillna(col.mean()) if col.name == 1 else col.fillna(0))
print(cleaned10)
print("-"*10)

cleaned11 = data.copy()
cleaned11[0] = cleaned11[0].fillna(cleaned11[2].mean())
print(cleaned11)
print("-"*10)

cleaned12 = data.replace(NA, 42)
print(cleaned12)
print("-"*10)

cleaned13 = data.apply(lambda col: col.fillna(np.random.uniform(1, 10)))
print(cleaned13)
print("-"*10)

cleaned14 = data.where(pd.notna(data), other=0)
print(cleaned14)
print("-"*10)

cleaned15 = data.copy()
cleaned15[1] = cleaned15[1].fillna(99)
print(cleaned15)
