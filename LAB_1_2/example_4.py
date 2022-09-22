import matplotlib.pyplot as plt
import numpy as np

x1 = [1,2,3,4]
y1 = [1,4,9,16]

x2 = [1,2,3,4]
y2 = [i**3 for i in x2]

# rows x cols = 2x2
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(6,6))

ax[0,1].plot(x1,y1,"go")
ax[0,1].set_title("Màu xanh lá")

ax[1,0].plot(x2,y2,"r^")
ax[1,0].set_title("Màu đỏ")

plt.show()

# Sinh viên tự vẽ ở ô [1,1] có y = 2*x với x = [1,2,3,4]

