# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:28:38 2021

@author: antona
https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html
"""
import numpy as np
import matplotlib.pyplot as plt
from pyts.image import RecurrencePlot


def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot Lorentz Attractor
#ax = plt.figure().add_subplot(projection='3d')

#ax.plot(xs, ys, zs, lw=0.5)

#ax.set_xlabel("X Axis")
#ax.set_ylabel("Y Axis")
#ax.set_zlabel("Z Axis")
#ax.set_title("Lorenz Attractor")
#plt.show()

# Select which partial derivative to represent by the plot
X =  np.array([xs])

# Recurrence plot transformation
rp = RecurrencePlot(threshold='point', percentage=20)
X_rp = rp.fit_transform(X)
plt.imshow(X_rp[0],  cmap='binary', origin='lower')
