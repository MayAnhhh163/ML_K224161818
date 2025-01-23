from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
# Prepare the dataset
data = {
    'x1': [7,3,5,8,9,5,4,2,8,6,9],
    'x2': [5,7,8,1,3,4,0,6,7,4,2],
    'y': [65,38,51,38,55,43,25,33,71,51,49]
}

df = pd.DataFrame(data)

# Split data into features (X) and target (y)
X = df[['x1', 'x2']]
y = df['y']

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_
sklearn_coefficients = [model.intercept_] + list(model.coef_)

print(mse, r2, coefficients, intercept)
print("Phương trình hồi quy (Sklearn): Y = {:.2f} + {:.2f}*X1 + {:.2f}*X2".format(*sklearn_coefficients))


