# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:04:25 2021

@author: aparn
"""

def print_msg(messege):
    greeting = "Hello"
    
    #inner function
    def printer():
        print(greeting,messege)
    return  printer 
        
return_fun =   print_msg("Python is Awesome ")
   
return_fun()