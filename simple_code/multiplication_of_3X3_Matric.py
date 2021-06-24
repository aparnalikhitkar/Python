# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 06:23:29 2021

@author: aparn
"""

import numpy as np
p = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
q = [[1, 2,3], [1, 2, 3], [1, 2, 3]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the said matrix multiplication:")
print(result1)
