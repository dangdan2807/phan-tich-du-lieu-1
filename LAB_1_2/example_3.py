# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:09:01 2022

@author: Student
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]

x2 = [1, 2, 3, 4]
y2 = [i**3 for i in x2]

# 1 dòng 2 cột
plt.subplot(1, 2, 1)
plt.plot(x1, y1, "go")
plt.title("Cột 1")

plt.subplot(1, 2, 2)
plt.plot(x2, y2, "r^")
plt.title("Cột 2")

plt.suptitle("Hiện thị 1 dòng 2 cột")
plt.show()

# Sinh viên tự viết 2 dòng 1 cột và hiện thị tương ứng
