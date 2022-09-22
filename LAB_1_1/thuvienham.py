# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:57:48 2020

@author: Administrator
"""

'''
File này là nơi viết các hàm cần thiết
'''

#Khai báo hàm kiểm tra một số là số nguyên tố

def isPrime(n):
    if(n < 0):
        return False
    elif(n == 0):
        return False
    elif(n == 1):
        return False
    elif(n == 2):
        return True
    else:
        for i in range(2,n):
            if(n % i == 0):
                return False
        return True