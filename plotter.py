import matplotlib.pyplot as pyplot
import computation

# plotting the functions
def plot_graphs(euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector,
                rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector):
    pyplot.plot(euler_x_vector, euler_y_vector, label="Euler")
    pyplot.plot(imp_euler_x_vector, imp_euler_y_vector, label="Improved Euler")
    pyplot.plot(rk_x_vector, rk_y_vector, label="Runge-Kutta")
    pyplot.plot(exact_x_vector, exact_y_vector, label="Exact")
    pyplot.legend(loc='lower left')
    pyplot.xlabel("X")
    pyplot.ylabel("Y")
    pyplot.show()


# plotting the local error function
# redundant parameters are for consistency
def plot_local_error_graphs(euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector,
                            rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector):
    euler_error_vector = [0] * len(euler_y_vector)
    imp_euler_error_vector = [0] * len(imp_euler_y_vector)
    rk_error_vector = [0] * len(rk_y_vector)

    for i in range(len(euler_error_vector)):
        euler_error_vector[i] = abs(exact_y_vector[i] - euler_y_vector[i])
        imp_euler_error_vector[i] = abs(exact_y_vector[i] - imp_euler_y_vector[i])
        rk_error_vector[i] = abs(exact_y_vector[i] - rk_y_vector[i])

    pyplot.plot(euler_x_vector, euler_error_vector, label="Euler")
    pyplot.plot(euler_x_vector, imp_euler_error_vector, label="Improved Euler")
    pyplot.plot(euler_x_vector, rk_error_vector, label="Runge-Kutta")
    pyplot.legend(loc='upper left')
    pyplot.xlabel("X")
    pyplot.ylabel("Error")
    pyplot.show()


# plotting the max error from N
def plot_max_error_graph(N, limit, IVPx, IVPy):


    euler_max_error_vector = []
    imp_euler_max_error_vector = []
    rk_max_error_vector = []


    err_x_vector = []

    for i in range(1, N):
        err_x_vector.append(i)

    for i in range(1, N):
        delta = float(float((limit - IVPx)) / i)
        if delta == 0: delta = float(1)

        euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector, \
        rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector = computation.compute(delta, IVPx, IVPy, limit)

        euler_error_vector, imp_euler_error_vector, rk_error_vector = computation.get_local_errors(euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector,
                         rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector)
        print(delta, max(euler_error_vector), max(imp_euler_error_vector), max(rk_error_vector))
        euler_max_error_vector.append(max(euler_error_vector))
        imp_euler_max_error_vector.append(max(imp_euler_error_vector))
        rk_max_error_vector.append(max(rk_error_vector))

    pyplot.plot(err_x_vector, euler_max_error_vector, label="Euler")
    pyplot.plot(err_x_vector, imp_euler_max_error_vector, label="Improved Euler")
    pyplot.plot(err_x_vector, rk_max_error_vector, label="Runge-Kutta")
    pyplot.legend(loc="upper left")
    pyplot.ylim(0, 25)
    pyplot.show()