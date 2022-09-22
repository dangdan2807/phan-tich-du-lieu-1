# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:31:22 2020

@author: Administrator
"""

#I/O trong Python - Kỹ thuật xử lý đọc file

# Dạng: Đọc file ---> đưa dữ liệu lên chương trình

'''
Hãy viết chương trình đọc file in.txt 
và hiển thị ra màn hình nội dung từng dòng
trong file đó
'''

fr = open('./DAY_1_TH/in.txt')
flines = fr.readlines()

for line in flines:
    print(line)
fr.close()


