# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:56:30 2020

@author: Amarnadh
"""
'''  Integers, Floats, Strings and Tuples are Immutable 
     Bcz., we cannot change the values therefore python creates new variable 
     with new memory address and with same name.  And it destoys the old
     memory address   
''' 
x=10
print("id(x)=",id(x)) # Printing the Memory address of x
x+=1
print("id(x)=",id(x))

'''  List, Set and Dictionaries are Mutable, therefore we can change
     the values and python wont creates a new memory address  '''
     
y=[10,20]  
print("List id(y)=",id(y)) # Printing the Memory address of y
y+=[30,40]
print("List id(y)=",id(y))

'''  Function parameters are also Mutable, therefore we can change
     the values and python wont creates a new memory address  '''

def show(a):
    print("id(a)=",id(a))
    a+=10
    print("id(a)=",id(a))

a=100
b=a
print("id(a)=",id(a),"id(b)=",id(b)) #gets same address
show(a)
print()

i=0
while i<=5:
    print("id(i)=",id(i))
    i+=1
print()

j=0
while j<=5:
    print("id(j)=",id(j))
    j+=1

x="india"
y="india"
print("id(x)=",id(x),"id(y)=",id(y))



