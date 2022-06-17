import numpy as np
import matplotlib.pyplot as plt

# constants
g, L = 1, 1
# define the bounds and resolution
res = 1/1000
theta, v = np.meshgrid(np.arange(-3*np.pi, 3*np.pi, res), np.arange(-2.5, 2.5, res))
# system of equations for phase plot
thetadot = v/L
vdot = -g/L*np.sin(theta)

# Controlling the starting points
# of the streamlines
#seek_pointx = -3*np.pi*np.ones(8)
#seek_pointy = [-1.4, -0.8,  -0.6, 0,-0.01 , 0.6, 0.8, 1.4]
#seek_points = np.array([seek_pointx, seek_pointy])

# plotting
plt.xticks(np.pi*np.arange(-3, 3+1, 1), [r"$-3\pi$", r"$-2\pi$", r"$-\pi$",
                                         r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$"])
plt.xlim(-3*np.pi, 3*np.pi)
plt.xlabel(r"$\vartheta$")
plt.ylabel(r"$v$")
#plt.plot(seek_pointx, seek_pointy, 'bo')
plt.streamplot(theta, v, thetadot, vdot, density=3, linewidth=0.5)
plt.grid()
plt.savefig("PendulumPhasePlot2.pdf")
