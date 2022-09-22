# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:54:22 2020

@author: Administrator
"""

#Phương pháp lập trình hàm trong Python
'''
Hãy nhập một số tự nhiên từ bàn phím
sau đó, xuất màn hình thông báo số đó
có phải là số nguyên tố hay không
'''

import thuvienham as lib

x = int(input('Nhập số tự nhiên: '))

if(lib.isPrime(x) == True):
    print('x là số nguyên tố')
else:
    print('x không là số nguyên tố')
