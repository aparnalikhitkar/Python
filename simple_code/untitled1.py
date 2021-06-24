# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:53:55 2021

@author: aparn
"""

def fib(num):
  """return the number at index num in the fibonacci sequence"""
  if num <= 2:
    return 1
  return fib(num - 1) + fib(num - 2)


print(fib(6))  # 8