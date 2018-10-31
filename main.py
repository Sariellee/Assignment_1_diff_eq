from Plot import *
from Computation import *
from tkinter import *

"""
Launches the app and initializes all the windows, buttons and entries.
"""
def main(app):
    app.winfo_toplevel().title("Diffur Master")
    head = Label(app, text="Numerical methods for equation sin^2(x) + y * ctg(x)")
    inp = Frame(app)

    IVPx = Frame(inp)
    IVPx_label = Label(IVPx, text="IVP(x)")
    default_IVPx = StringVar(app, value=1)
    IVPx_entry = Entry(IVPx, textvariable=default_IVPx)

    IVPy = Frame(inp)
    IVPy_label = Label(IVPy, text="IVP(y)")
    default_IVPy = StringVar(app, value=1)
    IVPy_entry = Entry(IVPy, textvariable=default_IVPy)

    limit = Frame(inp)
    limit_label = Label(limit, text="border(x)")
    default_limit = StringVar(app, value=3)
    limit_entry = Entry(limit, textvariable=default_limit)

    delta = Frame(inp)
    delta_label = Label(delta, text="step")
    default_delta = StringVar(app, value=0.5)
    delta_entry = Entry(delta, textvariable=default_delta)

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

    bttn_graphs.configure(
        command=lambda: handler(IVPx_entry.get(), IVPy_entry.get(), limit_entry.get(), delta_entry.get(), 0))
    bttn_error.configure(
        command=lambda: handler(IVPx_entry.get(), IVPy_entry.get(), limit_entry.get(), delta_entry.get(), 1))
    bttn_errN.configure(
        command=lambda: handler(IVPx_entry.get(), IVPy_entry.get(), limit_entry.get(), delta_entry.get(), 2))

    app.mainloop()


"""
Handles all the errors with the input and passes the parameters to the computation methods.
"""
def handler(IVPx, IVPy, limit, delta, mode):
    try:
        IVPx = float(IVPx)
        IVPy = float(IVPy)
        limit = float(limit)
        delta = float(delta)
    except:
        error = Label(app, text="Wrong input! Try using numbers")
        error.config(fg="red")
        error.pack()
        return
    if IVPx > limit:
        error = Label(app, text="Swap the IVPx and limit!")
        error.config(fg="red")
        error.pack()
        return
    if delta <= 0:
        if delta == 0:
            error = Label(app, text="Do you want me to divide by zero?")
        else:
            error = Label(app, text="Can't have negative step. Sorry mate")
        error.config(fg="red")
        error.pack()
        return
    if mode == 0:
        compute_graphs(IVPx, IVPy, limit, delta)
    if mode == 1:
        compute_error(IVPx, IVPy, limit, delta)
    if mode == 2:
        compute_errN(IVPx, IVPy, limit, delta)
    return


"""
Plots the solution graphs on a separate window
"""
def compute_graphs(IVPx, IVPy, limit, delta):
    solution = Computation(IVPx, IVPy, limit, delta)
    plotter = Plot("Plot")
    plotter.plot_graphs(solution.solution["Euler"][0], solution.solution["Euler"][1],
                        solution.solution["Improved Euler"][0], solution.solution["Improved Euler"][1],
                        solution.solution["Runge Kutta"][0], solution.solution["Runge Kutta"][1],
                        solution.solution["Exact"][0], solution.solution["Exact"][1])


"""
Plots the local error graphs in a separate window
"""
def compute_error(IVPx, IVPy, limit, delta):
    solution = Computation(IVPx, IVPy, limit, delta)
    plotter = Plot("Plot")
    plotter.plot_local_error_graphs(solution.solution["Euler"][0], solution.solution["Euler"][1],
                                    solution.solution["Improved Euler"][0], solution.solution["Improved Euler"][1],
                                    solution.solution["Runge Kutta"][0], solution.solution["Runge Kutta"][1],
                                    solution.solution["Exact"][0], solution.solution["Exact"][1])


"""
Plots the "Max error for step size" graph in a separate window"
"""
def compute_errN(IVPx, IVPy, limit, delta):
    plotter = Plot("Plot")
    plotter.plot_max_error_graph(limit, IVPx, IVPy, delta)


"""
Initialize the tkinter instance and pass it to main()
"""
if __name__ == '__main__':
    app = Tk()
    main(app)
