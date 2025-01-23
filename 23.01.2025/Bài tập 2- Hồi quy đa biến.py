import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dữ liệu
data = {
    'x1': [0.76, 4.25, 5.71, 3.58, 0.45, 0.13, 1, 0.76, 7.56, 0.76, 0.42, 2.93, 5.64, 3.93, 0.5, 0.2, 1.09, 1.95, 3.81, 5.41],
    'x2': [7.01, 14.45, 42.28, 11.13, 3, 63.46, 48.25, 24.8, 13.85, 50.46, 3.1, 11.21, 18.11, 21.56, 11.2, 7.62, 22.54, 44.38, 5.5, 11.73],
    'x3': [0.94, 0.84, 0.83, 0.24, 0.48, 0.18, 0.35, 0.34, 0.55, 0.43, 0.94, 0.53, 0.09, 0.43, 0.79, 0.33, 0.94, 0.9, 0.61, 0.29],
    'y': [33.52, 42.89, 12.04, 6.91, 6.57, 2.07, 4.18, 58.45, 29.64, 48.87, 33.75, 0.04, 16.75, 4.63, 61.69, 24.55, 32.9, 9.23, 11.4, 27.64]
}

# Tạo dataframe
df = pd.DataFrame(data)

# Ma trận X và Y
X = df[['x1', 'x2','x3']].values
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
print("Phương trình hồi quy (Sklearn): Y = {:.2f} + {:.2f}*X1 + {:.2f}*X2 + {:.2f}*X3".format(*sklearn_coefficients))

########################################
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
data = {
    'x1': [0.76, 4.25, 5.71, 3.58, 0.45, 0.13, 1, 0.76, 7.56, 0.76, 0.42, 2.93, 5.64, 3.93, 0.5, 0.2, 1.09, 1.95, 3.81, 5.41],
    'x2': [7.01, 14.45, 42.28, 11.13, 3, 63.46, 48.25, 24.8, 13.85, 50.46, 3.1, 11.21, 18.11, 21.56, 11.2, 7.62, 22.54, 44.38, 5.5, 11.73],
    'x3': [0.94, 0.84, 0.83, 0.24, 0.48, 0.18, 0.35, 0.34, 0.55, 0.43, 0.94, 0.53, 0.09, 0.43, 0.79, 0.33, 0.94, 0.9, 0.61, 0.29],
    'y': [33.52, 42.89, 12.04, 6.91, 6.57, 2.07, 4.18, 58.45, 29.64, 48.87, 33.75, 0.04, 16.75, 4.63, 61.69, 24.55, 32.9, 9.23, 11.4, 27.64]
}

df = pd.DataFrame(data)

# Split data into features (X) and target (y)
X = df[['x1', 'x2', 'x3']]
y = df['y']

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model1 = LinearRegression()
model1.fit(X_train, y_train)

# Make predictions
y_pred = model1.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Coefficients and intercept
coefficients = model1.coef_
intercept = model1.intercept_
sklearn_coefficients1 = [model1.intercept_] + list(model1.coef_)

print('MSE: ',mse,'\nR2: ',r2,'\ncoefficients: ',coefficients,'\nintercept: ',intercept)
print("Phương trình hồi quy (Sklearn): Y = {:.2f} + {:.2f}*X1 + {:.2f}*X2 + {:.2f}*X3".format(*sklearn_coefficients1))
