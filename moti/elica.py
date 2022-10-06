from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')

q, B, E, m = 1.6e-19, 2.5, 4, 1.67e-27
v = 0.1
a = E*q/m
R = m*v/(q*B)
t = np.linspace(0, 1e20, 50000)
yline = 0.5*a*(t**2)
xline=R*np.sin(q*B*t)
zline=R*(1-np.cos(q*B*t))
ax.view_init(elev=20, azim=10)
ax.plot(xline, yline, zline)
plt.show()
