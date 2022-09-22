# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:22:08 2020

@author: Administrator
"""

# Cấu trúc lặp: While, for
'''
Tính tổng s = 0 + 1 + ... + n, trong đó n 
là số tự nhiên nhập từ bàn phím
'''
# Cách 1: Sử dụng while

n = int(input('Nhập số n: '))

i = 0
s = 0 

while i <= n:
    s = s + i
    i = i+1
print('Tổng là: ',s)

