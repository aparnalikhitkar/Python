# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 06:01:04 2021

@author: aparn
"""

import numpy as np
x = np.ones((10,10))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")

x[1:-1,1:-1] = 0
print(x)


