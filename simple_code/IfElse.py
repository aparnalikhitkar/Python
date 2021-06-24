# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:52:24 2021

@author: aparn
"""

def product(x,y,z):
    if(x==7):
        temp = y*z
    elif(y==7):
        temp = z
    elif(z == 7):
        temp = -1
    else:
        temp = x*y*z
        
        return temp
a = int(input("Enter the 1st number  "))
b = int(input("Enter the 2nd number "))
c = int(input("Enter the 3rd number "))

p = product(a, b, c)                    
print("product =" , p);