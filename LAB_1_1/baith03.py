# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:36:48 2020

@author: Administrator
"""
#Bài luyện tập tổng hợp
'''
Viết chương trình tính tiền điện hàng tháng
Người sử dụng sẽ nhập số kWh từ bàn phím 
(là một số nguyên)
Chương tính như sau:
    1. Nếu số KhW nhỏ hơn bằng 100 
    thì đơn giá là 2000 VNĐ
    2. Nếu số KWh vượt 100, thì đơn giá cho 
    mỗi KWh sẽ được cộng dồn thêm 100 VNĐ
Ví dụ:
    Số Kwh = 90 thì tổng tiền = 180000 = 90 * 2000
    Số KWh = 101 thì tổng tiền = 202100 = 100 * 2000 + (2000 + 100)
    Số Kwh = 102 thì tổng tiền = 204300 = 100*2000 + (2000+100) + (2000+100+100)
'''
# range
# range(10) --> [0, 1, 2,3,4,5,6,7,8,9]
# range(2,9) --> [2,3,4,5,6,7,8]

# Hướng dẫn

soKwh = int(input('Nhập số KwH: '))

tongTien = 0

if soKwh <= 100:
    tongTien = soKwh * 2000
else:
    tongTien = 100*2000
    for i in range(1,soKwh-100+1):
        tongTien = tongTien + (2000+100*i)

print('Tổng tiền là: ',tongTien)
