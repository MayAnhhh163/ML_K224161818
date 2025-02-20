import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../dataset/USA_Housing.csv')
print(df.head())
print(df.info())
print(df.describe())
#sns.heatmap(df.corr()) ##xóa cột Address mới chạy đc code này

print(df.columns) #xuất tên cột
#Xây dựng và train mô hình dự báo
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

#Giả sử ở đây ta chi theo tỉ lệ 80% cho train và 20% cho test.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=101)

#Tạo và train mô hình
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

#Sử dụng mô hình
predictions = lm.predict(X_test)
print("Kết quả predict 20%: ")
print(predictions) #dùng để tính độ chính xác của mô hình

#predict từng căn nhà
pre1=lm.predict([X_test.iloc[0]])
print("kết quả =",pre1)

pre2=lm.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
print("kết quả 2 =",pre2)

#đánh giá mô hình
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

#xuất mô hình ra file zip
import pickle
modelname="../trainedmodel/housingmodel4.zip"
pickle.dump(lm, open(modelname, 'wb'))