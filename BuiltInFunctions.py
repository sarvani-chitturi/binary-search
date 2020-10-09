# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:25:22 2020

@author: Amarnadh
"""
x=[False,False,False,False]
print("all=",all(x))  #if any one value is false, then it retursn false
print("any=",any(x)) #if any one value is true, then it retursn true
print("ASCII char is ",chr(65))  #returns character of ASCII value
print("ord('A')=",ord('A')) #returns ASCII value of character
print("divmod 50/2 is ",divmod(50,2))  #returns quotient and remainder
print("id(2)=",id(2)) #gives the address of a number or variable
print("type(5)=",type(5))# returns the class to which the instance of obj belongs to
print("type(5.2)=",type(5.2))
print("isinstance=",isinstance(5.2,float))#returns bool value if obj is instance of a class or not
print("isinstance=",isinstance(5.5,int))
x = iter(["sachin", "dhoni", "virat"])#returns an iterator object
print(next(x),next(x),next(x)) #returns the next elm reported by iterator
x = iter([10, 20, 30])#returns an iterator object
print(next(x),next(x),next(x)) 
print("len('GITAM')=",len("GITAM"))#returns length of string or list
n=[100,200,300,400]
print("len(n)=",len(n))
print("max=",max(n))# returns max value
print("min=",min(n))# returns min value
print("pow(4,2)=",pow(4,3)) #returns 4 power 2
print("pow(5,3,2)=",pow(5,3,2)) #returns (5 power 3) mod 2
r=reversed([100,200,300,400])#reversed used to reverse the list
for i in r:
    print(i,end=' ')
print("\n",abs(-2))  #Gives a positive number
print("round(2.6789)=",round(2.6789))#returns the nearest value
print("round(2.6789,2)=",round(2.6789,2))#returns the value rounded to the nearest 10 pow -2
s=sorted([1,3,2,5,4,0])# used to sort the list in sequential order
for i in s:
    print(i,end=' ')
print()
print("sum(s)=",sum(s))

fp=open("hi.txt","r")#used to open the file with given name and access mode
r=input("Enter a value")  #reads the input value in the form of string
print("r=",r)#used to print the values


