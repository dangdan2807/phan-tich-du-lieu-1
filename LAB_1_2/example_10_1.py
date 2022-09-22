# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:45:35 2022

@author: hunagroup
"""

'''
Mảng và ma trận trong numpy
'''
import numpy as np

# Khai báo mảng có 12 phần tử 1,2,3,4,5,6,7,8,9,10,11,12
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)

# Câu hỏi 1: Mảng khác list chỗ nào?
# Câu hỏi 2: Tại sao dùng kiểu mảng trong thư viện numpy?

# Khai báo mảng hai chiều 2x6 (ma trận)
matrix = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(matrix)
print(matrix.ndim) # Số chiều
print(matrix.shape) # Kích thước (shape): (rows,cols) = (2,6)

matrix.shape = (3,4) # Chuyển đổi ma trận thành (rows,cols) = (3,4)
print(matrix)

matrix.shape = (2,-1) # Ma trận tự suy luận chiều còn lại là 6
print(matrix)

# NÂNG CAO
arr1 = np.arange(24) # tạo mảng có 24 phần tử có giá trị từ 0 đến 23
print(arr1)
arr1.shape = (2,12) # ma trận 2 chiều
print(arr1)
arr1.shape = (2,3,4) # ma trận 3 chiều
print(arr1)
arr1.shape = (2,2,2,3) # ma trận 4 chiều
print(arr1)
arr1.shape = (3,-1,2,2) # ma trận 4 chiều
print(arr1)
arr1.shape = (1,2,2,2,3) # ma trận 5 chiều
print(arr1)
arr1.shape = (1,2,2,2,3,1) # ma trận 6 chiều
print(arr1)
arr1.shape = (1,2,2,1,1,2,3,1) # ma trận 8 chiều
print(arr1)
# Câu hỏi: Cách biểu diễn ma trận n chiều trong numpy như thế nào?
# Câu hỏi: Làm sao để biết chuyển ma trận với n chiều là đúng






