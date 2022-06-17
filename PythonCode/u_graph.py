import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, np.pi/2, 1000)[1:-1]

# define the initial angle
theta_0 = 0.2

# define alpha
g, l, c = 1, 1, 1
a = 2*g*l/c**2

def u(x,theta_0):
    k = np.sin(theta_0/2)
    y = 2*a*k**2 * (np.cos(x))**2
    return (1- np.exp(-y))/y

def u_bad(x,theta_0):
    k = np.sin(theta_0/2)
    y = a*k**2 * (np.cos(x))**2
    return 1 - y + 2/3 * y*y
y1 = u(phi, 0.2)
y2 = u(phi, 0.5)
y3 = u(phi, 1)
y4 = u(phi, np.pi)
#y5 = u_bad(phi, np.pi)
plt.plot(phi, y1, label=r"$\vartheta_0 = 0.2$")
plt.plot(phi, y2, label=r"$\vartheta_0 = 0.5$")
plt.plot(phi, y3, label=r"$\vartheta_0 = 1$")
plt.plot(phi, y4, label=r"$\vartheta_0 = \pi$")
#plt.plot(phi, y5, label=r"$\vartheta_0 = \pi$")

plt.xticks([0, np.pi/4, np.pi/2], [r"$0$",r"$\pi/4$",r"$\pi/2$"])

plt.xlabel(r"$\phi$")
plt.ylabel(r"$u$")
plt.ylim(0, 1.01)
plt.xlim(0, np.pi/2)
plt.grid()
plt.legend()
plt.savefig("u_graph.pdf")