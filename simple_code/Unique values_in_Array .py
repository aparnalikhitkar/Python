# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 05:54:57 2021

@author: aparn
"""

import numpy as np
arr1 = np.array([0, 10, 20, 40, 60, 80])
arr2 = [10, 30, 40, 50, 70]
print("first Array: ",arr1)
print("second  Array: ",arr2)
print("Unique values in array 1 that are not in array2:")
print(np.setdiff1d(arr1, arr2))
