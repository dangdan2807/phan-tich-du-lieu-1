# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:29:36 2020

@author: Administrator
"""

# Cấu trúc lặp: While, for
'''
Tính tổng s = 0 + 1 + ... + n, trong đó n 
là số tự nhiên nhập từ bàn phím
'''
# Cách 2: Sử dụng for

n = int(input('Nhập số n: '))
s = 0

# Chú thích: range(n+1) --> [0, 1, 2....n]

for i in range(n+1):
    s = s + i
print('Tong la: ', s)
