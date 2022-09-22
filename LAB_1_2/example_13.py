# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:35:27 2022

@author: Student
"""

import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from random import randint

import numpy as np

fig, ax = plt.subplots()

data = np.linspace(-5,5,200)

ax.plot(data,data**2)

ax.set_xlim([-5,5])

ax.set_ylim([0,25])

pt, = plt.plot([-5],[25],'ro',ms=10)

def animate(i):

    x = data[i]

    y = x**2

    pt.set_data(x,y)

    #return pt

ani = FuncAnimation(fig, animate, frames =len(data), interval=100, repeat = False)

plt.show()