import mpmath as mp
import numpy as np
import matplotlib.pyplot as plt
mp.mp.dps = 20
g = mp.mpf('9.8')
L = mp.mpf('100000')
c = mp.mpf('300000000')
a = mp.mpf('2')*g*L/c**mp.mpf('2')
prefac = mp.mpf('4')*mp.sqrt(L/g)
theta_0 = mp.mpf('2.8')
initvel = mp.mpf('0')

f = mp.odefun(lambda x, y: [y[1], -g/L * (mp.mpf('1') - (L*y[1]/c)**2)*mp.sin(y[0])],
              0, [theta_0, initvel])

def Tr(theta_0):
    k = mp.sin(theta_0/mp.mpf('2'))
    def u(phi):
        x = 2*a*k**2 * (mp.cos(phi))**2
        return -mp.expm1(-x)/x  
    def integrand(phi):
        return 1/mp.sqrt(1 - (k*mp.sin(phi))**2) * 1/mp.sqrt(u(phi))
    return prefac*mp.quad(integrand, [0, mp.pi/2])


def theta(t):
    return f(t)[0]

def theta_dot(t):
    return f(t)[1]


end = float(Tr(theta_0))


t = np.linspace(0, end, 100)
arr_theta = []
for time in t:
    arr_theta.append(float(f(time)[0]))

#mp.plot(theta, [0, end], points = 20)
plt.plot(t, arr_theta)
plt.grid()
plt.xlim(0, end)
plt.xlabel(r"$t (s)$")
plt.ylabel(r"$\vartheta(t)$")
plt.savefig("theta_graph.pdf")
