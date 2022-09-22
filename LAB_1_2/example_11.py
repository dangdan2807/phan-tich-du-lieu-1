# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:14:24 2022

@author: Student
"""
'''
Hệ phương trình:
    
1*x - 2*y = -1 (1)
3*x + 5*y = 8 (2)

Ax = b
A: ma trận
b: vector
Yêu cầu: Giải nghiệm và trực quan nghiệm
'''

import numpy as np
import matplotlib.pyplot as plt

# Tính nghiệm
A = np.array([[1,-2],[3,5]])
b = np.array([-1,8])

ketqua = np.linalg.solve(A, b)
print("x0 = ", ketqua[0])
print("y0 = ", ketqua[1])

# Trực quan hóa

#Đường thẳng (1)
x1 = np.linspace(-2,2,50)
y1 = (x1+1)/2

#Đường thẳng (2)
x2 = np.linspace(-2,2,50)
y2 = (-3*x2 + 8)/5

plt.plot(x1,y1,x2,y2)
plt.show()

