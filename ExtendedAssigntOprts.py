# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:22:04 2020

@author: Amarnadh
"""

x=[10,20,30,40,50]
print("x=",x)
y=x
y+=[60,70] #in list this expression acts like a reference to list 'x'
print("x=",x)
y=y+[80,90]#in this case, it doesnt acts lika a reference to the list 'x'
print("x=",x)
print("y=",y)

a=3
a+=1
print(a)