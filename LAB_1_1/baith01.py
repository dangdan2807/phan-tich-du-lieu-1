# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:07:45 2020

@author: Administrator
"""

# Bài tập mẫu cơ bản

# Phần 1: Cấu trúc điều khiển: If...else

# Input ------ Process ----- Output

'''
Bài 1: Viết chương trình giải phương trình bậc 1
ax + b = 0, trong đó, a, b là các số thưc được nhập
từ bàn phím
'''
a = float(input('Nhập a: '))
b = float(input('Nhập b: '))

if a > 0 or a < 0:
    x = -b/a
    print('PT có nghiệm là: ', x)
else:
    if b == 0:
        print('PT có vô số nghiệm')
    else:
        print('PT vô nghiệm')
