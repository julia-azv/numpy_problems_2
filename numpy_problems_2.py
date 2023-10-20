# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 19:39:47 2023

@author: jazev
"""

import numpy as np

#exo1
#Write a NumPy program to create a vector with values from 0 to 20 and change 
#the sign of the numbers in the range from 9 to 15.
n = np.arange(21)
print("original vector",n)
n[9:16] = -n[9:16]
print("final vector",n)

#exo2
#Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
n=np.arange(15,56)
print("original vector",n)
n=n[1:-1]
print("final vector",n)

#exo3
#♥Write a NumPy program to create a 3X4 array and iterate over it.
a=np.array([[1,2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
for i in a:
  for j in i:
    print(j,end= " ")
  print()
  
#exo4
#Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
n = np.linspace(5, 50, 10)
print("final vector",n)

#exo5
#Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
n=np.random.randint(0,10,5)
print("final vector",n)

#exo6
#Write a NumPy program to multiply the values of two given vectors.
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
c=a*b
print(c)

#exo7
#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
a=np.random.randint(10,21,size=(3,4))
print(a)

#exo8
#Write a NumPy program to find the number of rows and columns in a given matrix.
a=np.array([[1,2,3,8],[4,5,6,2],[7,8,9,5]])
nbrows,nbcolumns=np.shape(a)
print("the number of rows is",nbrows,"and the number of colums is ",nbcolumns)

#exo9
#Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
a=np.zeros((4,4))
a[1::2, ::2] = 1
a[::2, 1::2] = 1
print(a)

#exo10
#Write a NumPy program to find common values between two arrays.
array1=[ 0,10,20,40,60]
array2=[10, 30, 40]
listcommon=[]
for element in array1:
  if element in array2:
    listcommon.append(element)
print("Common values between two arrays:",listcommon)

#exo11
#Write a NumPy program to get the unique elements of an array.
print("Original array")
original=[10,10,20,20,30,30]
print("Unique elements of the above array:")
unique=[]
for element in original:
  if element==element-1:
    unique.append(element)
print(unique)

#exo12
#Write a NumPy program to compute the cross product of two given vectors.
a=[1,2,3]
b=[6,7,8]
c=a[1]*b[2]-a[2]*b[1]
d=a[2]*b[0]-a[0]*b[2]
e=a[0]*b[1]-a[1]*b[0]
f=[c,d,e]
print("the cross product of a per b is ",f)

#exo13
#Write a NumPy program to convert cartesian coordinates to polar coordinates of a random 10x2 matrix representing
# cartesian coordinates.
cartesian_coords = np.random.rand(10, 2)
x = cartesian_coords[:, 0]
y = cartesian_coords[:, 1]

r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

theta_degrees = np.degrees(theta)

a = np.column_stack((r, theta_degrees))

print("Cartesian Coordinates:")
print(cartesian_coords)
print("\nPolar Coordinates:")
print(a)


#exo14
#Write a NumPy program to find the closest value (to a given scalar) in an array.
a = np.arange(100)
print("original vector",a)
value_to_compare = float(input("Enter the value that you want to compare: "))
print("\nValeur à comparer:", value_to_compare)
index = (np.abs(a - value_to_compare)).argmin()
closest_value = a[index]
print("Valeur la plus proche dans le tableau:", closest_value)



