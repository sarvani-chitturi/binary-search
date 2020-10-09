# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:12:56 2020

@author: Amarnadh
"""
#Keyword argument
def show(a,b,c):
    print("a=",a,"b=",b,"c=",c)
    
show(3,1,2)
show(c=3,a=1,b=2)
show(3,a=1,b=2)  #InValid bcz a is not allowed to assign mmultiple times
show(3,c=1,b=2)  #Valid


