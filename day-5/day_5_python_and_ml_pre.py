# -*- coding: utf-8 -*-
"""day-5-python-and-ml-pre.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13bFh5fL94LYtLGDdhCdTKPbxx4GifIFY
"""

import pandas as pd

data_1=pd.read_csv('/content/melb_data (1).csv')

data_1

data_1.head(10)

data_1.tail(10)

data_1.shape

data_1.info()

data_1.describe()

data_1.isnull().sum()

data_1.dropna()

?data_1.dropna()

import numpy as np
data_2=pd.DataFrame([[1,2,3,np.nan],[4,5,np.nan,np.nan],[np.nan, np.nan, np.nan, np.nan]])

data_2

data_3=data_2.dropna(how='all', inplace=True)

data_2

data_2.dropna(axis=1, thresh=2)

# delete columns which re having less than 13580 non null value
data_1.dropna(axis=1,thresh=13580)

data_2

data_fill = data_2.fillna(0) # fill empty values with 0

data_fill

data_1['Car'].fillna(data_1['Car'].mean())

data_1['YearBuilt'].fillna(data_1['Car'].mean(), inplace=True)

data_1['BuildingArea'].fillna(data_1['BuildingArea'].median(), inplace=True)

data_1.info()

data_1.fillna(method='ffill', inplace=True)

data_1.info()

outlier=pd.DataFrame([['x',20000],['y',100],['z',20],['e',30],['f',10000000]], columns=['name', 'marks'])

outlier

from scipy import stats
z=np.abs(stats.zscore(outlier.marks))

print(z)

# interquartile range
q1=outlier.quantile(0.25)
q2=outlier.quantile(0.75)
IQR=q2-q1
IQR

print((outlier<(q1-1.5*IQR))|(outlier>(q2+1.5*IQR)))

outlier=pd.DataFrame([['x',20000],['y',100],['z',20],['e',30],['f',10000000]], columns=['name', 'marks'])

outlier

outlier.replace(30,50) # replace value in DataFrame

outlier.replace({10:100, 30:200})