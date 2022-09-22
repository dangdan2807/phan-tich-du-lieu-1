# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 13:54:58 2022
@author: Student
"""

import matplotlib.pyplot as plt
sanPham = ['Sữa', 'Gạo', 'Đường', 'Nước ngọt', 'Muối']
doanhSo = [70, 82, 60, 55, 40]
_error = [5, 8, 7, 6, 4]

plt.barh(sanPham, doanhSo, xerr=_error, color='green')
plt.title('Thống kê doanh số')
plt.xlabel('Doanh số (triệu đồng)')
plt.ylabel('Danh mục')
plt.show()

# Câu hỏi đặt ra
'''
Cho ma trận: 
[[50,45,90,25,75]
[35,70,82,79,60]
[25,35,90,20,60]
[20,35,10,30,40]
[45,90,70,90,80]]

Mỗi cột tương ứng doanh số trong 5 tháng của các nhóm mặt hàng ['Sữa', 'Gạo', 'Đường', 'Nước ngọt', 'Muối']
Tạo mảng doanhSo = [?,?,?,?,?] tương ứng doanh số trung bình của các nhóm mặt hàng
Tạo mảng _error = [?,?,?,?,?] tương ứng cho độ lệch chuẩn của các nhóm mặt hàng
Vẽ biểu đồ barh biểu diễn doanhso và độ lệch chuẩn. 
'''
