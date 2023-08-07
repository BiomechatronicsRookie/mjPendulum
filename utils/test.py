import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.signal import chirp, step2
from RK45 import ode45

def mass_spring_damper(x, t, u, args):
    (b, k) = args
    p, v = x
    dydt = np.array([v, -b*v - k*p]) + u
    return dydt

def mass_spring_damper_odeint(x, t, *args):
    (b, k) = args
    p, v = x
    dydt = np.array([v, -b*v - k*p])
    return dydt

def pendulum(x, t, u, args):
    (g, l, b) = args
    th, w = x
    dydt = np.array([w, -b*w -g/l*np.sin(th)]) + u
    return dydt

def pendulum_odeint(x, t, *args):
    (g, l, b) = args
    th, w = x
    dydt = np.array([w, -b*w - g/l*np.sin(th)])
    return dydt

def exp_decay(x, t, u, args):
    (k,) = args
    dydt = -k*x + u
    return dydt

def exp_decay_odeint(x, t, *args):
    (k,) = args
    dydt = -k*x
    return dydt

h = 0.01
t_end = 10
t = np.arange(0,t_end,h)
x0 = np.array([3,0])
x00 = 1
x000 = np.array([np.pi/2, 0])

# Using ODEINT
mspd_odeint = odeint(mass_spring_damper_odeint, x0, t, args=(0.1, 7))
expd_odeint = odeint(exp_decay_odeint, x00, t, args=(1,))
pend_odeint = odeint(pendulum_odeint, x000, t, args=(9.8, 1.0, 0.01))

# Using RK45 implementation
mspd_RK4 = ode45(mass_spring_damper, x0, t, args=(0.1, 7))
expd_RK4 = ode45(exp_decay, x00, t, args=(1,))
pend_RK4 = ode45(pendulum, x000, t, args=(9.8, 1.0, 0.01))

_, ax = plt.subplots(1,3)
ax[0].plot(t,mspd_odeint[:,0])
ax[0].plot(t,mspd_RK4[:,0], '--')

ax[1].plot(t,expd_odeint)
ax[1].plot(t,expd_RK4, '--')

ax[2].plot(t,pend_odeint[:,0], label = 'Odeint')
ax[2].plot(t,pend_RK4[:,0],'--',label = 'RK4')

_.supxlabel('t(s)')
_.supylabel('Amplitude (-)')
_.suptitle('Comparison of integrators')
ax[2].legend()
plt.show()