import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import control as ctrl
import sys
from RK45 import ode45

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

class Pendulum():
    def __init__(self,m1,m2,l,g,b):
        self.m1 = m1
        self.m2 = m2
        self.l = l 
        self.g = g
        self.b = b

    def dynamics(self, x, t, u = None, args = None):
        (g, l, b) = args
        th, w = x
        dydt = np.array([w, -b*w -g/l*np.sin(th)]) + u
        return dydt
    
    def sym(self, x0, t_):
        self.states = ode45(self.dynamics, x0, t_, args=(self.g, self.l, self.b))


def main():
    ##---------- Nonlinear Dynamics ----------
    # Model Parameters
    m1 = 1
    m2 = 1 
    l = 1
    g = 9.8 
    b = 0.1
    t_ = np.arange(0,5,0.001)
    x0 = np.array([np.pi/2, 0])

    # Object definition and simulation
    p = Pendulum(m1,m2,l,g,b)
    p.sym(x0, t_)

    # Plot results
    fig, ax = plt.subplots(1,2)
    ax[0].plot(t_,p.states[:,0])
    ax[1].plot(t_,p.states[:,1])
    plt.show()

if __name__=='__main__':
    main()


