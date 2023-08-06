import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pylab import *
import time
import control as ctrl

def annimate_simulation(data, dt):

    fig, ax  = plt.subplots()
    ax.set_xlim(min(data)-0.1, max(data)+0.1)

    line = ax.scatter([],[],s = 20, c = 'b', marker='s')
    time_text = ax.text(0.05, 0.9, '', transform = ax.transAxes)
    def animate(i):
        time_text.set_text(f"time = {dt*i:1f}s")
        line.set_offsets(np.c_[data[i], 0])
        return line, time_text,

    ani = FuncAnimation(fig, animate, len(data)-1, interval = dt*1000, repeat = False, blit = True)
    ani.save('animation.gif', writer = 'PillowWriter', fps = 25, dpi = 100)

    return

# Model Parameters
m = 0.5
k = 20
b = 1

# State space description
A = np.array([[0, 1],[-k/m, -b/m]])
B = np.array([0, 1/m])
C = np.array([[1, 0]])
D = 0

# State space and step function simulation
sys = ctrl.ss(A,B,C,D)
t = np.linspace(0,5,501)
h = np.diff(t[::5])[0]
step = ctrl.step_response(sys,t)

# Plot result of step function
annimate_simulation(step.y[0].ravel()[::5],h)



