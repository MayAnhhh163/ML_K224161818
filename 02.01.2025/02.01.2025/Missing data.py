#Lọc dữ liệu bị thiếu
from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)

cleaned = data.dropna()
print(cleaned)
print("-"*10)

cleaned2=data.dropna(how='all')
print(cleaned2)
print("-"*10)

cleaned3=data.dropna(how='any')
print(cleaned3)
print("-"*10)

cleaned4 = data.dropna(subset=[1])  # Xóa hàng nếu cột 1 có giá trị thiếu
print(cleaned4)
print("-"*10)

cleaned5 = data.dropna(thresh=2)  # Giữ hàng có ít nhất 2 giá trị không thiếu
print(cleaned5)
print("-"*10)

cleaned6 = data[data[0].notna()]  # Lọc các hàng mà cột đầu tiên không bị thiếu
print(cleaned6)
print("-"*10)

data_filled = data.fillna(0)  # Thay NA bằng 0
cleaned7 = data_filled[data_filled[0] != 0]  # Lọc giá trị các hàng mà cột đầu khác 0
print(cleaned7)
print("-"*10)

cleaned8 = data[data[1].isna()]
print(cleaned8)
print("-"*10)

cleaned9 = data[data[1] == 1]
print(cleaned9)
print("-"*10)

cleaned10 = data.dropna(axis=1)
print(cleaned10)
print("-"*10)

