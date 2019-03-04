import matplotlib.pyplot as plt
from matplotlib import animation
import os

class Animator:
    def __init__(self,X_MIN,X_MAX,Y_MIN,Y_MAX):
        self.X_MIN = X_MIN
        self.X_MAX = X_MAX
        self.Y_MIN = Y_MIN
        self.Y_MAX = Y_MAX
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(X_MIN, X_MAX), ylim=(Y_MIN, Y_MAX), title="Curve Fitting", xlabel="x", ylabel="y")
        self.line, = self.ax.plot([], [], lw=1)
        self.degree_text = self.ax.text(0.5, 0.95, '', horizontalalignment='center', transform=self.ax.transAxes)
        self.error_text = self.ax.text(0.5, 0.90, '', horizontalalignment='center', transform=self.ax.transAxes)
        self.X, self.Y, self.err = None, None, None

    def init_frame(self):
        self.line.set_data([], [])
        self.degree_text.set_text('')
        self.error_text.set_text('')
        return self.line, self.degree_text, self.error_text

    def animate(self,i):
        self.line.set_data(self.X, self.Y[i])
        self.degree_text.set_text('Degree = {}'.format(i))
        self.error_text.set_text('Error = {}'.format(self.err[i][0]))
        return self.line, self.degree_text, self.error_text

    def visualize_data(self,x_in,fx_in,x_out,y_out,error):
        self.X = x_out
        self.Y = y_out
        self.err = error
        self.ax.plot(x_in,fx_in,'-o',lw=1)
        degrees,_ = y_out.shape
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_frame,
                                       frames=degrees, interval=1000, blit=True)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        anim.save('{}/curve_fit.gif'.format(dir_path), dpi=80, writer='imagemagick', fps = 30)
        plt.show()