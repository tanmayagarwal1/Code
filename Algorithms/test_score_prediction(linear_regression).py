import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#READING THE DATASET 
#DATASET FROM - https://drive.google.com/open?id=1oakZCv7g3mlmCSdv9J8kdSaqO5_6dIOw

dataset = pd.read_csv('D:\Datasets\student_scores.csv')
dataset.shape
dataset.head()
dataset.describe()

#PREPARING THE DATA 

dataset.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#TRAINING AND TESTING 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)

#PREDICTIONS 

y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df