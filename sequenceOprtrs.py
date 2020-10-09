# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:54:56 2020

@author: Amarnadh
"""

x=[10,20,30,40,50]
print(x)
# prints the complete list
 
print(x[0:5]) 
#0 is starting index position and 4 is total elements to print
 
print(x[0:5:2])
#0 is starting index position and 5 is total elements to print 
 #  and 2 is steps to skip
 
print(x[-1])
#prints the last element

print(x[-2])
#prints the last but one element

y=[100,200,300]
print(x+y)
#concatenate x and y list together

print(2*x) 
#print the x list twice

del x[4]
print(x)
#deleted 4th index position from the list 'x' i.e., 50

if(10 in x):#checking 10 in the 'x' list or not
    print("Yes")
else:
    print("No")
    
if(100 not in x):#checking 100 in the 'x' list or not
    print("Yes")
else:
    print("No")

