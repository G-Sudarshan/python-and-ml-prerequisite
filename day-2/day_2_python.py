# -*- coding: utf-8 -*-
"""day-2-python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iR_OtFI61LFYzGvc-4eWRPrnVR7b1uNH
"""

# tuples
tup1 = ("Sudarshan", 23, "march", 2001)
tup2 = 1,2,3,4,5

print(tup1)
print(tup2)

tup3 = tup1 + tup2
print(tup3)

tup4 = tup1 * 2
print(tup4)

if "march" in tup1:
  print("present in tup1")
else:
  print("not present in tup1")

# create 5 diffrent tuples 

tup1 = ("jan", "feb", "march", "april", "may")
tup2 = (10, 20, 30, 40, 50)
tup3 = ("apple", 100, "mango", 200)
tup4 = 12, 34, 45, 567
tup5 = "hp", "dell", "lenovo", "apple", "asus"

list1 = ["a","b","c","d","e"]

print(len(tup1))
print(max(tup4))
print(min(tup2))
tup = tuple(list1)
print(tup)

# slicing of tuples

tup1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

print(tup1[1:4])
print(tup1[:5])
print(tup1[:-4])

my_tuple = ('a', 'p', 'p', 'l', 'e')

if 'p' in my_tuple:
  print("present in my tuple")
  count = 0
  for p in my_tuple:
    if p == 'p':
      count = count + 1
  print("p appears in tuple {0} times".format(count))

# list
my_list = ['Sudarshan', 'tony', 'steve', 2001, 23, 3]
print(my_list)
my_list[2] = 'bruce'
print(my_list)

list_1 = ["sudarshan"]
list_2 = [100, 200, 300, 400, 500]
list_3 = [234, 34, 56, 69, 23]

print(len(list_2))
print(max(list_3))
print(min(list_3))
print(list_1 * 5)

for i in list_2:
  print(i//100)

print(list_2 + list_3)

# list methods
list_1 = [10, 20, 30, 40]

list_1.append(50)
print(list_1)

list_2 = list_1.copy()
print(list_2)

print(list_1.count(20))

list_1.extend([60, 70, 80])
print(list_1)

print(list_1.index(30))

# dictionary: combination of key-value pair
d1 = {1: 'apple', 2: 'ball'}
print(d1)

car = {
    "brand": "Toyota",
    "model": "New Delhi",
    "Year": 2020,
    "Country": "India",
    1: 2021
}

print(car)
print(car.get("brand"))

car.pop("model")
print(car)

car.popitem()
print(car)

print(car.keys())

car.clear()
print(car)

d2 = d1.copy()
print(d2)

d3 = { 10: "hi"}
print(d3)

d3.update(d1)
print(d3)

# functions
def print_this():
  print("Hello World")

def add(a, b):
  sum = a + b
  print("sum is:",sum)


print_this()
add(19,56)

def add(a, b):
  sum = a + b
  mul = a * b
  return sum, mul


print(add(12,21))