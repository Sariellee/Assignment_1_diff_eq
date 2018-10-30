from Plot import *
from Computation import *
from tkinter import *

deltaa = 0.22222  # our step
limita = 4  # rightmost interval border
IVPxa = 1  # X of IVP
IVPya = 1  # Y of IVP


def main():
    app = Tk()
    head = Label(app, text="Numerical methods for equation sin^2(x) + y * ctg(x)")
    inp = Frame(app)

    IVPx = Frame(inp)
    IVPx_label = Label(IVPx, text="IVP(x)")
    IVPx_entry = Entry(IVPx)

    IVPy = Frame(inp)
    IVPy_label = Label(IVPy, text="IVP(y)")
    IVPy_entry = Entry(IVPy)

    limit = Frame(inp)
    limit_label = Label(limit, text="border(x)")
    limit_entry = Entry(limit)

    delta = Frame(inp)
    delta_label = Label(delta, text="step")
    delta_entry = Entry(delta)

    buttn = Frame(app)
    bttn_graphs = Button(buttn, text="Plot the solution graphs")
    bttn_error = Button(buttn, text="Plot the error graphs")
    bttn_errN = Button(buttn, text="Plot the 'max error for every N' graph")

    head.pack()

    IVPx_label.pack()
    IVPx_entry.pack()
    IVPx.pack()

    IVPy_label.pack()
    IVPy_entry.pack()
    IVPy.pack()

    limit_label.pack()
    limit_entry.pack()
    limit.pack()

    delta_label.pack()
    delta_entry.pack()
    delta.pack()

    inp.pack()

    bttn_graphs.pack()
    bttn_error.pack()
    bttn_errN.pack()
    buttn.pack()

    bttn_graphs.configure(command=lambda: compute_graphs(float(IVPx_entry.get()), float(IVPy_entry.get()), float(limit_entry.get()), float(delta_entry.get())))
    bttn_error.configure(command=lambda: compute_error(float(IVPx_entry.get()), float(IVPy_entry.get()), float(limit_entry.get()), float(delta_entry.get())))
    bttn_errN.configure(command=lambda: compute_errN(float(IVPx_entry.get()), float(IVPy_entry.get()), float(limit_entry.get()), float(delta_entry.get())))

    app.mainloop()


def compute_graphs(IVPx, IVPy, limit, delta):
    solution = Computation(IVPx, IVPy, limit, delta)
    plotter = Plot("Plot")
    plotter.plot_graphs(solution.solution["Euler"][0], solution.solution["Euler"][1],
                        solution.solution["Improved Euler"][0], solution.solution["Improved Euler"][1],
                        solution.solution["Runge Kutta"][0], solution.solution["Runge Kutta"][1],
                        solution.solution["Exact"][0], solution.solution["Exact"][1])


def compute_error(IVPx, IVPy, limit, delta):
    solution = Computation(IVPx, IVPy, limit, delta)
    plotter = Plot("Plot")
    plotter.plot_local_error_graphs(solution.solution["Euler"][0], solution.solution["Euler"][1],
                                    solution.solution["Improved Euler"][0], solution.solution["Improved Euler"][1],
                                    solution.solution["Runge Kutta"][0], solution.solution["Runge Kutta"][1],
                                    solution.solution["Exact"][0], solution.solution["Exact"][1])


def compute_errN(IVPx, IVPy, limit, delta):
    plotter = Plot("Plot")
    plotter.plot_max_error_graph(limit, IVPx, IVPy, delta)


if __name__ == '__main__':
    main()
