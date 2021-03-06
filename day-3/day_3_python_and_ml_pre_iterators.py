# -*- coding: utf-8 -*-
"""day3-python-and-ml-pre-iterators.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lx1iLfc-lfWq66nG3RF9FBDMxaAJvLet
"""

# to iterate over iteratable objects
a = [10, 20, 30, 40, 50]
print(a)

var = 'python'

for i in var:
  print(i)

var = 'python'

iter_obj = iter(var)
print(iter_obj)

for i in a:
  print("index is", a.index(i), "Value is", i)

for i in range(len(a)):
  print(i, a[i])

a

sum = 0
for i in a:
  sum = sum + i

print(sum)

b = ['a', 'v', 'd', 'r']
for i in b:
  print(i)

print(type(b))

# iterate dictionary
stu = {
    'name': 'sudarshan',
    'roll_no': '23384'
}

print(stu)
print(stu.keys())
print(stu.values())

for k, v in stu.items():
  print(k, v)

# list of list and iterate it
l = [[10, 20], [30, 40], [50, 60], [70, 80]]

for i in l:
  for j in i:
    print(j)

t1 = (1, 2, 3, 4, 5)
print(t1)

for i in t1:
  print(i)

for i, v in enumerate(a):
  print(i, v)

import statistics as st
import math
import scipy.stats as sc

x = [10, 12.5, 50, 60, 100]
sum = 0
for i in x:
  sum = sum + i

mean = sum / len(x)
print(mean)

st.mean(x)

st.median(x)

x1 = [45, 56, 700, 500, 400, 550]
len(x1)

st.median(x1)

var2 = ['suresh', 'ajay', 'rohini', 'ojas', 'swapnil', 'geeta', 'ajay']
st.mode(var2)

sc.mode(var2)

v1 = [15, 78, 12, 63, 99, 100, 450, 100, 260, 150]
len(v1)

st.variance(v1)

st.pvariance(v1)

st.stdev(v1)

st.pstdev(v1)

x = [1.23, 2.12, 3.34, 4.5]
y = [2.56, 2.89, 3.76, 3.95]

import numpy as np

cov_mat = np.stack((x,y), axis=0)

cov_mat

np.cov(cov_mat)

np.corrcoef(x,y)

np.ptp(x)

x2 = [12, 50, 60, 75, 90]
np.quantile(x2, .25)

np.quantile(x2, .50)

np.quantile(x2, .75)