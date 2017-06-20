# zombie apocalypse modeling
import numpy as np
from scipy.integrate import odeint

import matplotlib.pyplot as plt
import pylab


a = 0.5

A = 0.0001  # destroy percent  (per day)
p = np.random.sample(size=11)
print(p)
# x = np.array([1])
# yc = np.array([0.5])
# Ac = np.vstack([x, np.ones(len(x))]).T
# m, c = np.linalg.lstsq(Ac, yc)[0]
# print(np.linalg.lstsq(Ac, yc))
b = 0.25
c = 0.25


# solve the system dy/dt = f(y, t)
def f(y, t):
    A = y[0]
    Ne = y[1]
    G1 = y[2]
    S = y[3]
    G2M = y[4]
    # the model equations (see Munz et al. 2009)
    f0 = p[5] * G1 + p[4] * S + b * p[3] * G2M - p[10] * A
    f1 = a * p[2] * G2M - (p[0] + p[5] + p[6]) * G1
    f2 = p[0] * G1 - (p[4] + p[7] + p[1]) * S
    f3 = p[1] * S - (a * p[2] + b * p[3] + c * p[8]) * G2M
    f4 = p[6] * G1 + p[7] * S + c * p[8] * G2M - p[9] * Ne
    return [f0, f1, f2, f3, f4]


# initial conditions
A0 = 10
Ne0 = 2
G10 = 56
S0 = 6
G2M0 = 50
y0 = [A0, Ne0, G10, S0, G2M0]  # initial condition vector
t = np.linspace(0, 1, 100)  # time grid

# solve the DEs
soln = odeint(f, y0, t)
A = soln[:, 0]
Ne = soln[:, 1]
G1 = soln[:, 2]
S = soln[:, 3]
G2M = soln[:, 4]
print(soln[:, 4])
# plot results
plt.plot(t, A, label='Living', color='red')
plt.plot(t, G1, label='asdg', color='green')
plt.plot(t, G2M, label='124', color='blue')
plt.plot(t, S, label='sah', color='yellow')
plt.plot(t, Ne, label='svjh', color='grey')
plt.show(block=True)

# # change the initial conditions
# R0 = 0.01 * S0  # 1% of initial pop is dead
# y0 = [S0, Z0, R0]
#
# # solve the DEs
# soln = odeint(f, y0, t)
# S = soln[:, 0]
# Z = soln[:, 1]
# R = soln[:, 2]
#
# plt.figure()
# plt.plot(t, S, label='Living')
# plt.plot(t, Z, label='Zombies')
# plt.xlabel('Days from outbreak')
# plt.ylabel('Population')
# plt.title('Zombie Apocalypse - 1% Init. Pop. is Dead; No New Births.')
# plt.legend(loc=0)
#
# # change the initial conditions
# R0 = 0.01 * S0  # 1% of initial pop is dead
# P = 10  # 10 new births daily
# y0 = [S0, Z0, R0]

# solve the DEs
# soln = odeint(f, y0, t)
# S = soln[:, 0]
# Z = soln[:, 1]
# R = soln[:, 2]
#
# plt.figure()
# plt.plot(t, S, label='Living')
# plt.plot(t, Z, label='Zombies')
# plt.xlabel('Days from outbreak')
# plt.ylabel('Population')
# plt.title('Zombie Apocalypse - 1% Init. Pop. is Dead; 10 Daily Births')
# plt.legend(loc=0)
