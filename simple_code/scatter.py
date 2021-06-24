# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:38:03 2021

@author: aparn
"""
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y = [2,5,6,7,8,9,10,3]
plt.scatter(x,y,label="Scatterplot", color='r' ,s=25,marker = "o")

plt.title("first line chart ") 
plt.xlabel("Student roll number ")
plt.ylabel("Age of  Student  ")
plt.legend()
plt.grid(False)
plt.show()