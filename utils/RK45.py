import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def RK45step(fun, x, t, u, h, args):
    k1 = fun(x,t,u,args)
    k2 = fun(x + (h/2)*k1, t + (h/2), u, args)
    k3 = fun(x + (h/2)*k2, t + (h/2), u, args)
    k4 = fun(x + h*k3, t + h, u, args)
    xk1 = x + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return xk1

def ode45(fun, x0, t, u = None, args = None):
    if type(x0) == float or type(x0) == int:
        if u is None:
            u = np.zeros(len(t))
        res = np.zeros(len(t))
        res[0] = x0
        h = np.diff(t)[0]
        for i in range(len(t)-1):
            res[i+1] = RK45step(fun, res[i], t[i], u[i], h, args)
        res = res.T
    else:
        if u is None:
            u = np.zeros((x0.shape[0],len(t)))
        res = np.zeros((x0.shape[0],len(t)))
        res[:,0] = x0
        h = np.diff(t)[0]
        for i in range(len(t)-1):
            res[:,i+1] = RK45step(fun, res[:,i], t[i], u[:,i], h, args)
        res = res.T
    return res

if __name__=='__main__':

    def fun(x, t, u, args):
        (k,) = args
        dxdt = -k*x + u
        return dxdt
    
    def fun_ode(x, t, *args):
        (k,) = args
        dxdt = -k*x
        return dxdt
    
    h = 0.01
    t = np.arange(0,10,h)
    inp = np.random.rand(len(t))*10
    res = ode45(fun, 10.0, t, inp, args=(1,))
    res2 = ode45(fun, 10.0, t, args=(1,))
    res3 = odeint(fun_ode, 10.0, t, args=(1,))
    _, ax = plt.subplots()
    ax.plot(t, res, label='Decay + Noise Input')
    ax.plot(t, res2, label = 'Decay' )
    ax.plot(t, res3, '--', label = 'Decay Odeint' )
    ax.legend()
    plt.show()
   