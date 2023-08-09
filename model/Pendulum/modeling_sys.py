import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import control as ctrl
import sys
from RK45 import ode45

class Pendulum():
    def __init__(self,m1,m2,l,g,b):
        self.m1 = m1
        self.m2 = m2
        self.l = l 
        self.g = g
        self.b = b

    def dynamics(self, x, t, u = None, *args):
        (g, l, b) = args
        th, w = x
        dydt = np.array([w, -b*w -g/l*np.sin(th)]) + u
        return dydt
    
    def sym(self, x0, t_):
        self.states = ode45(self.dynamics, x0, t_, args=(self.g, self.l, self.b))

    def forward_kinematics(self):
        q = self.states[:,0]
        self.data = np.array([self.l*np.sin(q), -self.l*np.cos(q)])
    
    def annimate(self, dt, fps, file_name):
        fig, ax  = plt.subplots()
        ax.set_xlim(min(self.data[0,:])-0.1, max(self.data[0,:])+0.1)
        ax.set_ylim(min(self.data[1,:])-0.1, max(self.data[1,:])+0.1)
        ax.grid()
        ax.set_aspect('equal', 'box')
        line, = ax.plot([], [], lw = 1, marker='o', color = 'b')
        time_text = ax.text(0.05, 0.9, '', transform = ax.transAxes)

        def animate(i):
            time_text.set_text(f"time = {dt*i:1f}s")
            line.set_data([0,self.data[0,i]], [0,self.data[1,i]])
            return line, time_text,

        ani = FuncAnimation(fig, animate, max(self.data.shape), interval = dt*1000, repeat = False, blit = True)
        ani.save(file_name, writer = 'PillowWriter', fps = fps, dpi = 100)


def main():
    ##---------- Nonlinear Dynamics ----------
    # Model Parameters
    m1 = 1
    m2 = 1 
    l = 1
    g = 9.8 
    b = 0.3
    h = 0.02
    t_ = np.arange(0,10,h)
    
    x0 = np.array([np.pi/2, 0])

    # Object definition and simulation
    p = Pendulum(m1,m2,l,g,b)
    p.sym(x0, t_)
    p.forward_kinematics()

    # Plot results
    fig, ax = plt.subplots(1,2)
    ax[0].plot(t_,p.states[:,0])
    ax[1].plot(t_,p.states[:,1])
    plt.show()

    p.annimate(h, 1/h,'./model/Pendulum/pendulum_animation.gif')


if __name__=='__main__':
    main()


