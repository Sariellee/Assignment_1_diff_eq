import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Plot import *
from Computation import *
import tkinter

delta = 0.22222  # our step
limit = 4  # rightmost interval border
IVPx = 1  # X of IVP
IVPy = 1  # Y of IVP


class app(Tk):

    def compute_graphs(self):
        solution = Computation(IVPx, IVPy, limit, delta)
        plotter = Plot("Plot")
        plotter.plot_graphs(solution.solution["Euler"][0], solution.solution["Euler"][1],
                            solution.solution["Improved Euler"][0], solution.solution["Improved Euler"][1],
                            solution.solution["Runge Kutta"][0], solution.solution["Runge Kutta"][1],
                            solution.solution["Exact"][0], solution.solution["Exact"][1])
        plotter.plot_local_error_graphs(solution.solution["Euler"][0], solution.solution["Euler"][1],
                                        solution.solution["Improved Euler"][0], solution.solution["Improved Euler"][1],
                                        solution.solution["Runge Kutta"][0], solution.solution["Runge Kutta"][1],
                                        solution.solution["Exact"][0], solution.solution["Exact"][1])
        plotter.plot_max_error_graph(10, 4, 1, 1)

        canvas1 = FigureCanvasTkAgg(
            plotter.plot_graphs(solution.solution["Euler"][0], solution.solution["Euler"][1],  # exchange for variable
                                solution.solution["Improved Euler"][0], solution.solution["Improved Euler"][1],
                                solution.solution["Runge Kutta"][0], solution.solution["Runge Kutta"][1],
                                solution.solution["Exact"][0], solution.solution["Exact"][1]), self)
        canvas1.get_tk_widget().place(x=470, y=20)

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry('900x700')
        self.title = "Plotter"
        self.resizable(width=False, height=False)
        self.compute_graphs()


if __name__ == '__main__':
    app = app()
    while True:
        try:
            app.mainloop()
        except UnicodeDecodeError:
            continue
