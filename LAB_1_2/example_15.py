import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from random import randint

import numpy as np

data = np.linspace(-5,5,200)

x = []

y = []

fig, ax = plt.subplots()

def animate(i):

    temp = data[i]

    x.append(temp)

    pt = temp**2

    y.append(pt)

    
    ax.clear()

    ax.plot(x,y)

    ax.set_xlim([-5,5])

    ax.set_ylim([0,25])

    
ani = FuncAnimation(fig, animate, frames =200, interval=100, repeat = False)

plt.show()