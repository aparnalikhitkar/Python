# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:33:05 2021

@author: aparn
"""

from matplotlib import pyplot as plt
#%matplotlib inline
#plotting to our canvas 

x = [5,8,10,7,34,56,78,46,89,34,78]
y = [10,15,20,25,30,35,45,50,60,70,80,85,90]


#plt.plot(x, y)

plt.hist(x,y,histtype="bar",rwidth=9.0)

#showing what we plotted
plt.title("first line chart ") 
plt.xlabel("Student roll number ")
plt.ylabel("Age of  Student  ")
plt.legend()
plt.grid(False)
plt.show()
