# -*- coding: utf-8 -*-
"""Day-9-python-and-ml-pre.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1izmj7mFJQ0fTkqhEySxsyMl2vPjyYco7
"""

import pandas as pd

dataset=pd.read_csv('/content/Salary_Data.csv')
dataset.count()

dataset.head()

dataset.describe()

dataset.info()

import matplotlib.pyplot as plt
plt.plot(dataset);

import seaborn as sns
sns.scatterplot(x=dataset['YearsExperience'],y=dataset['Salary']);

# split the dataset into training and testing 
# define x and y

X=dataset.iloc[:,:-1].values # all rows escept last column
y=dataset.iloc[:,-1].values # all rows with only last column

print(X)

print(y)

# split dataset into training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.7,test_size=0.3,random_state=0)

# help(train_test_split)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

regressor.intercept_

regressor.coef_

y=b0+b1x1
salary=26777+9360*yearsofExperience

# predict x_test values
y_pred=regressor.predict(X_test)
y_pred

y_test

print(X_test)

salary=26777+9360*9.5
salary

plt.scatter(X_train,y_train,color='red');
plt.plot(X_train, regressor.predict(X_train),color='blue')
plt.title('Salary Vs Experience(Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show();

# visualise the test set
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary Vs Experience(Testing Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

from sklearn.metrics import r2_score
# we will make prediction for y values

y_train_pred=regressor.predict(X_train)
y_test_pred=regressor.predict(X_test)

print(r2_score(y_train, y_train_pred))
print(r2_score(y_test, y_test_pred))