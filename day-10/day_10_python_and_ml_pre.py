# -*- coding: utf-8 -*-
"""Day-10-python-and-ml-pre.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c0L9WGWQf0LaBHX6hl2klyuJm0CA8ZiD
"""

import pandas as pd

#import/load dataset
dataset=pd.read_csv('/content/50_Startups.csv')

dataset.head()
dataset.shape

dataset.info()

dataset.head()

# Import matplotlib and seaborn libraries to visualize the data
import matplotlib.pyplot as plt 
import seaborn as sns

# Using pairplot we'll visualize the data for correlation
sns.pairplot(dataset, x_vars=['R&D Spend', 'Administration','Marketing Spend'], 
             y_vars='Profit', size=4, aspect=1, kind='scatter')
plt.show()

# Visualizing the data using heatmap
sns.heatmap(dataset.corr(), cmap="YlGnBu", annot = True)
plt.show()

#Define X and Y

X=dataset.iloc[:,:-4]
y=dataset.iloc[:,-1]
print(X[0:5])
print(y[0:5])

#split the dataset into training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.7,test_size=0.3, random_state=0)

print(X_train.count())

print(X_test.count())

print(y_train.count())

print(y_test.count())

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()  # create the object of regressor
regressor.fit(X_train,y_train)

# Intercept value
print("Intercept :",regressor.intercept_)

# Slope value
print('Slope :',regressor.coef_)

#The straight-line equation we get for the above values is,
#profit =  intercept + slope * R&D

#predict
y_pred=regressor.predict(X_test)
print(y_pred)
print(y_test)
print(y_pred-y_test)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')

from sklearn.metrics import r2_score
# Making Predictions of y_value
y_train_pred = regressor.predict(X_train)
y_test_pred = regressor.predict(X_test)

# Comparing the r2 value of both train and test data
print(r2_score(y_train,y_train_pred))
print(r2_score(y_test,y_test_pred))

#the R² value on test data is within 5% of the R² value on training data.
# We can apply the model to the unseen test set in the future.