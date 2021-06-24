# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:37:09 2021

@author: aparn
"""
#define a decorator 
def  hello_decorator(func):
    #inner1 is a Wrapper Function in 
    #inner function can access the outer local 
    #function like in this case "func "
    def inner1():
        print("Hello , this is before function execution ")
        #calling the actual function now 
        #inside the wrapper function 
        func()
        print("this is after fuction execution")
    return inner1
# defining a function to be called inside wrapper
def function_to_be_used():
    print("I am new Functionality ")
    print("this is inside the function")

#passing 'funtion_to_be_used' inside the decorater to control its behavior 
function_to_be_used =  hello_decorator(function_to_be_used)
#calling the function 
function_to_be_used()