import mpmath as mp
mp.mp.dps = 100
# define constants
g = mp.mpf('9.8')
L = mp.mpf('100000')
c = mp.mpf('300000000')

# derived constants
a = mp.mpf('2')*g*L/c**mp.mpf('2')

M = mp.sqrt(mp.mpf('2')*a/(mp.mpf('1') - mp.exp(-mp.mpf('2')*a)))

prefac = mp.mpf('4')*mp.sqrt(L/g)


theta_0 = mp.pi
k = mp.sin(theta_0/mp.mpf('2'))
def u(phi):
    x = 2*a*k**2 * (mp.cos(phi))**2
    return -mp.expm1(-x)/x  

def integrand(phi):
    return 1/mp.sqrt(1 - (k*mp.sin(phi))**2) * 1/mp.sqrt(u(phi))





mp.plot(integrand, [0, mp.pi/2], points=200, file="IntegrandGraph.pdf")
    