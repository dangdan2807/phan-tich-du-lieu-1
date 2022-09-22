import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from random import randint

import numpy as np

fig, ax = plt.subplots()

data = np.linspace(-5,5,200)

ax.plot(data,data**2)

ax.set_xlim([-5,5])

ax.set_ylim([0,25])


# Vẽ hình tròn

circle = plt.Circle((0,0), 0.5, fc='r')

def init():

    circle.center = (-5,25)    

    ax.add_patch(circle)

    return circle

def animate(i):

    x = data[i]

    y = x**2

    circle.center = (x,y)

    return circle

ani = FuncAnimation(fig, animate, init_func=init ,frames =len(data), interval=100, repeat = False)

plt.show()