import numpy as np
from Visualize import Animator


def get_function():
    fs = 100  # sample rate
    f = 2  # the frequency of the signal
    x = np.arange(fs)  # the points on the x axis for plotting
    # compute the value (amplitude) of the sin wave at the for each sample
    y = np.sin(2*np.pi*f * (x/fs))
    return x,y


def fit_curve(x,y,deg=1):
    z,residuals,_,_,_ = np.polyfit(x, y, deg, full=True)
    p = np.poly1d(z)
    return p, residuals


if __name__ == "__main__":
    x, fx = get_function()

    fit_results = [fit_curve(x,fx,d) for d in range(30)]

    interval = np.ptp(x)

    X = np.arange(x[0]-interval,x[-1]+interval)
    Y = np.c_[[poly(X) for poly,err in fit_results]]
    err = np.c_[[err for poly,err in fit_results]]

    viewer = Animator(X_MIN=min(min(X),min(x)), X_MAX=max(max(X),max(x)), Y_MIN=1.5*min(fx), Y_MAX=1.5*max(fx))
    viewer.visualize_data(x,fx,X,Y,err)
