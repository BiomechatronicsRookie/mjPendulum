import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pylab import *
import time
import control as ctrl
from scipy.integrate import odeint

def annimate_simulation(data, dt, fps):
    
    fig, ax  = plt.subplots()
    ax.set_xlim(min(data[0,:])-0.1, max(data[0,:])+0.1)
    ax.set_ylim(min(data[1,:])-0.1, max(data[1,:])+0.1)
    ax.grid()
    ax.set_aspect('equal', 'box')
    line = ax.scatter([],[],s = 20, c = 'b', marker='s')
    time_text = ax.text(0.05, 0.9, '', transform = ax.transAxes)

    def animate(i):
        time_text.set_text(f"time = {dt*i:1f}s")
        line.set_offsets(np.c_[data[0,i], data[1,i]])
        return line, time_text,

    ani = FuncAnimation(fig, animate, max(data.shape), interval = dt*1000, repeat = False, blit = True)
    ani.save('./model/CartPole/animation.gif', writer = 'PillowWriter', fps = fps, dpi = 100)

    return

##---------- Nonlinear Dynamics ----------
# Model Parameters
m1 = 1
m2 = 1 
l = 1
g = 9.8 
b = 1
T = 2
class Pendulum():
    def __init__(self,m1,m2,l,g,b):
        self.m1 = m1
        self.m2 = m2
        self.l = l 
        self.g = g
        self.b = b
        self.T = T

    def dynamics(self,y, t, g, l):
        th, w = y
        dydt = [w, -g/l*np.sin(th)]
        return dydt

    def sym(self, y0, t):
        self.sol = odeint(self.dynamics, y0, t, args=(self.g,self.l))
        return 

p1 = Pendulum(m1,m2,l,g,b)
h = 0.02
t_ = np.arange(0,T,h)
fps = 1/h
p1.sym(np.array([np.pi/2,0]), t_)

annimate_simulation(np.array([l*sin(p1.sol[:,0]),-l*cos(p1.sol[:,0])]),h,fps)



