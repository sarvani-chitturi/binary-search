# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 00:13:23 2020

@author: Amarnadh
"""
'''
if the user enters the values in the same line then we can use split() method
and here we have the give the input only in single line but not in mutli line
'''

reply = input( "Enter x and y, separated by spaces: ")
pieces = reply.split( ) # returns a list of strings, as separated by spaces
x = float(pieces[0])
y = float(pieces[1])
print("x=",x)
print("y=",y)