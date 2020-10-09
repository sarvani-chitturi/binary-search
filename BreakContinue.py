# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:21:36 2020

@author: Amarnadh
"""
print("Break Statement")
for i in range(1,11):  #prints 1 to 5 numbers
    print(i,end=' ')#end is used to print values in same line
    if i==5:
        break

print("\nContinue Statement")
x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    if i%2==0:
        continue
    print(i,end=' ')
    
    
    
