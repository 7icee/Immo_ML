import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("processed_dataset.csv")
data = data.drop(['kitchen', 'terraceSurface', 'Population'], axis=1)

#Attempts to improve model

def remove_outliers_iqr(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column_name] >= lower_bound) & (df[column_name] <= upper_bound)]

data = remove_outliers_iqr(data, 'price') # Step 1 : From 0.18 to 0.446
data = remove_outliers_iqr(data, 'livingArea') #Step 2 : From 0.446 to 484

X = data.drop(columns=['price'])  # Features
y = data['price']                # Target


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'mae = {mae}')
print(f'mse = {mse}')
print(f'r2 = {r2}')

corr = data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()