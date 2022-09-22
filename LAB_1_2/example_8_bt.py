# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

sanPham = ['Sữa', 'Gạo', 'Đường', 'Nước ngọt', 'Muối']
maTran = [[50, 45, 90, 25, 75],
          [35, 70, 82, 79, 60],
          [25, 35, 90, 20, 60],
          [20, 35, 10, 30, 40],
          [45, 90, 70, 90, 80]]

doanhSo = []
for item in maTran:
    doanhSo.append(np.sum(item))

print('Doanh số:', doanhSo)

_error = [5, 8, 7, 6, 4]

plt.barh(sanPham, doanhSo, xerr=_error, color='green')
plt.title('Thống kê doanh số')
plt.xlabel('Doanh số (triệu đồng)')
plt.ylabel('Danh mục')
plt.show()