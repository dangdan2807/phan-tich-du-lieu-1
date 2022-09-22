# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:38:01 2022

@author: Student
"""

import matplotlib.pyplot as plt
import numpy as np

x = [167,170,149,165,155]
y = [86,74,66,78,68]

plt.xlim(140,180)
plt.ylim(60,90)
# Sinh viên tự ylim dựa trên dữ liệu

plt.scatter(x, y)
plt.xlabel("Ox")
plt.ylabel("Oy")

plt.show()