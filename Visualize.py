import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

class Animator:
    def __init__(self,X_MIN,X_MAX,Y_MIN,Y_MAX):
        self.X_MIN = X_MIN
        self.X_MAX = X_MAX
        self.Y_MIN = Y_MIN
        self.Y_MAX = Y_MAX
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(X_MIN, X_MAX), ylim=(Y_MIN, Y_MAX), title="Polynomial Curve Fitting", xlabel="x", ylabel="y")
        # self.ax.grid()
        self.line, = self.ax.plot([], [], lw=1)
        self.degree_text = self.ax.text(0.25, 0.95, '', transform=self.ax.transAxes)
        self.error_text = self.ax.text(0.25, 0.90, '', transform=self.ax.transAxes)
        self.x, self.y, self.err = None, None, None


    def init_frame(self):
        self.line.set_data([], [])
        self.degree_text.set_text('')
        self.error_text.set_text('')
        return self.line, self.degree_text, self.error_text

    def animate(self,i):
        self.line.set_data(self.x, self.y[i])
        self.degree_text.set_text('Degree = {}'.format(i))
        self.error_text.set_text('Error = {}'.format(self.err[i][0]))
        return self.line, self.degree_text, self.error_text

    def visualize_data(self,x_in,fx_in,y_in,error):
        self.x = x_in
        self.y = y_in
        self.err = error
        self.ax.plot(x_in,fx_in,'-o',lw=1)
        degrees,_ = y_in.shape
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_frame,
                                       frames=degrees, interval=1000, blit=True)
        anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

        plt.show()