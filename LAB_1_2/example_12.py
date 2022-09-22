# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:27:24 2022

@author: Student
"""

'''
Tính giá trị của đạo hàm f(x) = x^2 tại x0 = 1
'''
from math import *

def f(x):
    return x**2

def derive(func, value):
    h = 0.00000000001
    tuso = func(value + h) - func(value)
    mauso = h
    
    return tuso/mauso
    
'''
Tính giá trị của đạo hàm f(x) = x^2 tại x0 = 1
'''
kq = derive(f, 1)
print(kq)

