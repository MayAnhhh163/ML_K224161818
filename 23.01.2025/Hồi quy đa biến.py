import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dữ liệu
data = {
    'x1': [7, 3, 5, 8, 9, 5, 4, 2, 8, 6, 9],
    'x2': [5, 7, 8, 1, 3, 4, 0, 6, 7, 4, 2],
    'y': [65, 38, 51, 38, 55, 43, 25, 33, 71, 51, 49]
}

# Tạo dataframe
df = pd.DataFrame(data)

# Ma trận X và Y
X = df[['x1', 'x2']].values
Y = df['y'].values.reshape(-1, 1)

# Bước 1: Tính các đại lượng cần thiết
X_with_intercept = np.hstack([np.ones((X.shape[0], 1)), X])  # Thêm cột 1 vào X để biểu diễn hệ số chặn

X_transpose = X_with_intercept.T  # Ma trận chuyển vị của X
XTX = np.dot(X_transpose, X_with_intercept)  # X'X
XTX_inv = np.linalg.inv(XTX)  # (X'X)^(-1)
XTY = np.dot(X_transpose, Y)  # X'Y

# Tính vector hệ số hồi quy B_hat
B_hat = np.dot(XTX_inv, XTY)

# Bước 2: Xây dựng phương trình hồi quy
def regression_equation(B):
    equation = f"Y = {B[0][0]:.2f}"
    for i, coef in enumerate(B[1:], start=1):
        equation += f" + {coef[0]:.2f}*X{i}"
    return equation

regression_eq = regression_equation(B_hat)

# Bước 3: Kiểm tra với Sklearn
model = LinearRegression()
model.fit(X, Y.ravel())
sklearn_coefficients = [model.intercept_] + list(model.coef_)

# In kết quả
print("Ma trận X'X:\n", XTX)
print("Ma trận (X'X)^(-1):\n", XTX_inv)
print("Ma trận X'Y:\n", XTY)
print("Vector B_hat:\n", B_hat)
print("Phương trình hồi quy (tự tính):", regression_eq)
print("Phương trình hồi quy (Sklearn): Y = {:.2f} + {:.2f}*X1 + {:.2f}*X2".format(*sklearn_coefficients))
