# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:17:58 2020

@author: Amarnadh
                FILE MODES
"r" - Read - will read a file, returns an error if the file does not exit 

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

"x" - Create - will create a file, returns an error if the file exist

"""

fp=open("demo.txt","r")#file opened from current direcotry to read the text
fp=open("C:\Python\PythonClasses\demo.txt","r")#file opened to read the text through path
print(fp.read())
print(fp.read(5)) #Returns the first 5 characters of the file
print(fp.readline()) #Returns one line
print(fp.readline()) #Returns one 2nd line
#if we use readline() twice then it returns tow lines

print(fp.readlines()) #Returns the (remaining) contents of a readable file as a string.
for line in fp:
    print(line)
fp.seek(5) #used to change the current position to be at 5th byte of a file
print(fp.tell()) #Return the current pointer position 
print(fp.read())
fp.close() #closes the file

fp1=open("demo1.txt","w")#file opened to write or to override the text 
fp1.write("I love my country")
fp1.writelines(["I love my Country","India"])#writes the items of a list to the file.
fp1.write(input("Enter your text"))# writes the text given at run time through keyboard
fp1.close()

fp2=open("demo2.txt","a")#file opened to write or append the text
fp2.write("Gitam University")
fp1.writelines(["I love my Country","India"])
fp1.write(input("Enter your text"))
fp2.close()

fp3=open("demo3.txt","x")#file opened to write and return error if the file exit
fp3.write("INDIA WON THE 2011 ICC WORLD CUP")
fp1.writelines(["I love my Country","India"])
fp1.write(input("Enter your text"))
fp3.close()



