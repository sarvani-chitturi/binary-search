# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:21:36 2020

@author: Amarnadh
"""
print("Method 1")
for i in range(1,6):  #prints 1 to 5 numbers
    print(i,end=' ')#end is used to print values in same line

print("\nMethod 2")
x=[10,20,30,40,50]
for i in x:
    print(i,end=' ')
    
print("\nMethod 3")
x=[10,20,30,40,50]
for i in range(len(x)):
    print(x[i],end=' ')

print("\nMethod 4")
x=[10,20,30,40,50]
for i in range(1,len(x)):
    print(x[i],end=' ')
    
print("\nMethod 5")
x=[10,20,30,40,50,60,70,80,90,100]
for i in range(0,len(x),4):
    print(x[i],end=' ')

