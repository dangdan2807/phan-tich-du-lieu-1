# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:04:34 2022

@author: Student
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = [1,2,3,4]
y1 = [1,4,9,16]

x2 = [1,2,3,4]
y2 = [i**3 for i in x2]

# y2 = [1,8,27,64]

plt.plot(x1,y1,'go',x2,y2,'r^')

plt.title("Hai đồ thị")
plt.xlabel("Trục Ox")
plt.ylabel("Trục Oy")

plt.show()