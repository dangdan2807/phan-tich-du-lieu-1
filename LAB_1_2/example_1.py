# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,4,9,16]

plt.figure(figsize=(15,5))

plt.title("Đồ thị")
plt.xlabel("Trục Ox")
plt.ylabel("Trục Oy")

plt.plot(x,y, "go") #go = green o
plt.show()
