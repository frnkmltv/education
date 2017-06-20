# 3D heat equation


import numpy as np
from numpy import exp, sqrt

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
fig.set_dpi(100)
axes = Axes3D(fig)

x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)

X, Y = np.meshgrid(x, y)

# Initial time
t0 = 0

# Time increment
dt = 0.05

# Initial temperature at (0,0) at t0=0
T = 1

# Sigma squared
s = 2


# Temperature function
def u(x, y, t):
    return (T / sqrt(1 + 4 * t / s)) * exp(-(x ** 2 + y ** 2) / (s + 4 * t))


a = []

for i in range(500):
    z = u(X, Y, t0)
    t0 = t0 + dt
    a.append(z)

m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
m.set_array(a[0])
cbar = plt.colorbar(m)

k = 0


def animate(i):
    global k
    temp = a[k]
    k += 1
    axes.clear()
    axes.plot_surface(X, Y, temp, rstride=1, cstride=1, cmap=plt.cm.jet, linewidth=0, antialiased=False)

    # ax1.contour(x,y,temp)
    axes.set_zlim(0, T)
    axes.set_xlim(-5, 5)
    axes.set_ylim(-5, 5)


anim = animation.FuncAnimation(fig, animate, frames=220, interval=20)
plt.show()
