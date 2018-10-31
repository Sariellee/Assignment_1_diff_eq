import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as pyplot
from Computation import *
from matplotlib.figure import Figure


class Plot:

    def __init__(self, title):
        self.figure = Figure(dpi=70)
        self.figure.suptitle(title)

    """
    plotting the functions
    """

    def plot_graphs(self, euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector,
                    rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector):
        pyplot.figure()
        pyplot.plot(euler_x_vector, euler_y_vector, label="Euler")
        pyplot.plot(imp_euler_x_vector, imp_euler_y_vector, label="Improved Euler")
        pyplot.plot(rk_x_vector, rk_y_vector, label="Runge-Kutta")
        pyplot.plot(exact_x_vector, exact_y_vector, label="Exact")
        pyplot.legend(loc='lower left')
        pyplot.suptitle("Solution graph")
        pyplot.xlabel("X")
        pyplot.ylabel("Y")
        pyplot.show()

    # plotting the local error function
    # redundant parameters are for consistency
    def plot_local_error_graphs(self, euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector,
                                rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector):
        euler_error_vector = [0] * len(euler_y_vector)
        imp_euler_error_vector = [0] * len(imp_euler_y_vector)
        rk_error_vector = [0] * len(rk_y_vector)

        for i in range(len(euler_error_vector)):
            euler_error_vector[i] = abs(exact_y_vector[i] - euler_y_vector[i])
            imp_euler_error_vector[i] = abs(exact_y_vector[i] - imp_euler_y_vector[i])
            rk_error_vector[i] = abs(exact_y_vector[i] - rk_y_vector[i])
        pyplot.figure()
        pyplot.plot(euler_x_vector, euler_error_vector, label="Euler")
        pyplot.plot(euler_x_vector, imp_euler_error_vector, label="Improved Euler")
        pyplot.plot(euler_x_vector, rk_error_vector, label="Runge-Kutta")
        pyplot.legend(loc='upper left')
        pyplot.suptitle("Error graph")
        pyplot.xlabel("X")
        pyplot.ylabel("Error")
        pyplot.show()

    # plotting the max error from N
    def plot_max_error_graph(self, limit, IVPx, IVPy, delta):

        euler_max_error_vector = []
        imp_euler_max_error_vector = []
        rk_max_error_vector = []

        err_x_vector = []

        N = int((limit - IVPx) / delta)

        for i in range(1, N):
            err_x_vector.append(i)

        for i in range(1, N):
            delta = float(float((limit - IVPx)) / i)
            if delta == 0: delta = float(1)

            computer = Computation(IVPx, IVPy, delta, limit)

            euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector, \
            rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector = computer.compute(delta, IVPx, IVPy, limit)

            euler_error_vector, imp_euler_error_vector, rk_error_vector = computer.get_local_errors(euler_x_vector,
                                                                                                    euler_y_vector,
                                                                                                    imp_euler_x_vector,
                                                                                                    imp_euler_y_vector,
                                                                                                    rk_x_vector,
                                                                                                    rk_y_vector,
                                                                                                    exact_x_vector,
                                                                                                    exact_y_vector)
            print(delta, max(euler_error_vector), max(imp_euler_error_vector), max(rk_error_vector))
            euler_max_error_vector.append(max(euler_error_vector))
            imp_euler_max_error_vector.append(max(imp_euler_error_vector))
            rk_max_error_vector.append(max(rk_error_vector))
        pyplot.figure()
        pyplot.plot(err_x_vector, euler_max_error_vector, label="Euler")
        pyplot.plot(err_x_vector, imp_euler_max_error_vector, label="Improved Euler")
        pyplot.plot(err_x_vector, rk_max_error_vector, label="Runge-Kutta")
        pyplot.suptitle("Error-Step size graph")
        pyplot.xlabel("Step size")
        pyplot.ylabel("Error")
        pyplot.legend(loc="upper left")
        pyplot.show()
