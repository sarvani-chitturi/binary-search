# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 09:07:06 2020

@author: Amarnadh
"""

a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))

if a<b:
    if a<c:
        print(a,"is small")
    else:
        print(c,"is small")
elif b<a:
    if b<c:
        print(b,"is small")
    else:
        print(c,"is small")
else:
    print(c,"is small")
