# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:27:14 2022

@author: Student
"""

import matplotlib.pyplot as plt
import numpy as np

x = [20, 30, 50, 60, 70, 80, 90, 100]
y = [8, 6, 4, 12, 18, 16, 20, 10]

plt.xticks(range(0, 100, 1))
# Sinh viên tự viết yticks sao cho khoảng nhảy là 1

plt.scatter(x, y)
plt.xlabel("Ox")
plt.ylabel("Oy")

plt.show()
