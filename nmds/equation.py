import scipy as sp

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.cm import get_cmap


class Heat_Equation(object):
    """
    Class which implements a numerical solution of the 2d heat equation
    """

    def __init__(self, dx, dy, a, timesteps=1000):
        self.dx = dx  # Interval size in x-direction.
        self.dy = dy  # Interval size in y-direction.
        self.a = a  # Diffusion constant.
        self.timesteps = timesteps  # Number of time-steps to evolve system.
        self.dx2 = dx ** 2
        self.dy2 = dy ** 2
        self.nx = int(1 / dx)
        self.ny = int(1 / dy)
        self.w = None
        # For stability, this is the largest interval possible
        # for the size of the time-step:
        self.dt = self.dx2 * self.dy2 / (2 * a * (self.dx2 + self.dy2))
        self.u, self.ui = self.get_initial_conditions()

    def get_initial_conditions(self):
        # Start u and ui off as zero matrices:
        ui = sp.zeros([self.nx, self.ny])
        u = sp.zeros([self.nx, self.ny])
        # Now, set the initial conditions (ui).
        for i in range(self.nx):
            for j in range(self.ny):
                p = i * self.dx + j * self.dy2
                if p <= 0.01 and p >= .005:
                    ui[i, j] = 1
        return u, ui

    def evolve_ts(self):
        self.u[1:-1, 1:-1] = self.ui[1:-1, 1:-1] + self.a * self.dt * (
            (self.ui[2:, 1:-1] - 2 * self.ui[1:-1, 1:-1] + self.ui[:-2, 1:-1]) / self.dx2 + (
                self.ui[1:-1, 2:] - 2 * self.ui[1:-1, 1:-1] + self.ui[1:-1, :-2]) / self.dy2)
        self.ui = self.u.copy()


# def evolve_ts(u, ui):
#     global nx, ny
#     """
#     This function uses two plain Python loops to
#     evaluate the derivatives in the Laplacian, and
#     calculates u[i,j] based on ui[i,j].
#     """
#     for i in range(1, nx - 1):
#         for j in range(1, ny - 1):
#             uxx = (ui[i + 1, j] - 2 * ui[i, j] + ui[i - 1, j]) / dx2
#             uyy = (ui[i, j + 1] - 2 * ui[i, j] + ui[i, j - 1]) / dy2
#             u[i, j] = ui[i, j] + dt * a * (uxx + uyy)


# In[5]:


test_heat = Heat_Equation(0.01, 0.01, .5, 1)

# First set up the figure, the axis, and the plot element we want to animate


fig = plt.figure()
img = plt.subplot(111)

im = img.imshow(test_heat.ui, cmap=get_cmap("hot"), interpolation='nearest', origin='lower')
im.figure = fig
fig.colorbar(im)


def animate(i, im):
    if i % 50 == 0:
        print i
    test_heat.evolve_ts()
    im.set_array(test_heat.ui)

    return [im]


anim = animation.FuncAnimation(fig, animate, frames=2000, fargs=(im,), interval=30, blit=True)
plt.show()
