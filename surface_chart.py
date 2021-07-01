import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D


class SurfaceChart(FigureCanvas):
    def __init__(self):
        self.fig =plt.figure(figsize=(7,7))
        FigureCanvas.__init__(self, self.fig)
        self.axes = self.fig.gca(projection='3d')
        self.setWindowTitle("Main")

    def draw_graph(self, x, y, z):
        self.axes.clear()
        self.axes.plot_surface(x, y, z, cmap=cm.coolwarm, alpha=0.75,
                       linewidth=0, antialiased=True)
        self.draw()
        self.axes.set_xlabel("x")
        self.axes.set_ylabel("y")
        self.axes.set_zlabel("z")

    def draw_simplex(self, args):
        x1, y1, z1, x2, y2, z2, x3, y3, z3, color = args
        self.axes.plot([x1, x2, x3, x1], [y1, y2, y3, y1], [z1, z2, z3, z1], color=color, linewidth=2)
        self.draw()