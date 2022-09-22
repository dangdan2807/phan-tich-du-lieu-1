# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:05:00 2022

@author: Student
"""

#Biểu đồ Gant biểu diễn tiến độ
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlim(0,160)

ax.set_ylim(0,50)

ax.set_xlabel('Ngày công')

ax.set_ylabel('Dự án')

ax.set_yticks([15,25,35])

ax.set_yticklabels(['Dự án 1','Dự án 2', 'Dự án 3'])

ax.grid(True)

ax.broken_barh([(40,50)],(30,8), facecolors=('tab:orange'))

ax.broken_barh([(10,50),(100,20),(130,10)],(20,8), facecolors=('tab:red'))

ax.broken_barh([(20,10),(50,30), (100, 50)],(10,8), facecolors=('tab:blue'))

plt.show()

#chiều dài của hình nhật, chiều rộng của hình chữ nhật.