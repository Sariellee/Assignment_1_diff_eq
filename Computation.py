import math

class Computation:

    solution = {}

    def __init__(self, IVPx, IVPy, limit, delta):

        sol = self.compute(delta, IVPx, IVPy, limit)

        self.solution["Euler"] = (sol[0], sol[1])
        self.solution["Improved Euler"] = (sol[2], sol[3])
        self.solution["Runge Kutta"] = (sol[4], sol[5])
        self.solution["Exact"] = (sol[6], sol[7])


    # function as is
    def funct(self, x, y):
        if math.tan(x) == 0:
            return 99999999
        else:
            return pow(math.sin(x), 2) + y * pow(math.tan(x), -1)


    # calculating IVP based on exact solution of the equation
    def calculate_c(self, x, y):
        if math.sin(x) == 0:
            return 99999999
        return (math.sin(x) * math.cos(x) + y) / math.sin(x)


    # analytically solved equation
    def exact(self, x, c):
        return c * math.sin(x) - math.sin(x) * math.cos(x)


    # def funct14(x, y):
    #     return pow(y, 4) * math.cos(x) + y * math.tan(x)
    #
    #
    # def exact14(x):
    #     return pow(1 / (-3 * math.sin(x) * pow(math.cos(x), 2) + pow(math.cos(x), 3)), 1 / 3)

    # euler method for solving the equation numerically
    def euler(self, x_vector, y_vector, delta, limit):
        i = x_vector[0] + delta  # we always start from the IVP, so 1st element after it would be IVP+delta
        ind = 1  # we always start from index 1, that is the first value after the IVP
        while i <= limit:
            x_vector[ind] = i

            # The method formula itself
            y_vector[ind] = y_vector[ind - 1] + delta * (self.funct(x_vector[ind - 1], y_vector[ind - 1]))
            i += delta
            ind += 1
        return x_vector, y_vector


    # improved euler method for solving the equation numerically
    def improved_euler(self, x_vector, y_vector, delta, limit):
        i = x_vector[0] + delta  # we always start from the IVP, so 1st element after it would be IVP+delta
        ind = 1  # we always start from index 1, that is the first value after the IVP
        while i <= limit:
            x_vector[ind] = i

            # The method formula itself
            k = y_vector[ind - 1] + delta * self.funct(x_vector[ind - 1], y_vector[ind - 1])
            y_vector[ind] = y_vector[ind - 1] + delta / 2 * (
                    self.funct(x_vector[ind - 1], y_vector[ind - 1]) + self.funct(x_vector[ind], k))
            i += delta
            ind += 1
        return x_vector, y_vector


    # Runge-Kutta method for solving the equation numerically
    def runge_kutta(self, x_vector, y_vector, delta, limit):
        i = x_vector[0] + delta  # we always start from the IVP, so 1st element after it would be IVP+delta
        ind = 1  # we always start from index 1, that is the first value after the IVP
        while i <= limit:
            x_vector[ind] = i

            # The method formula itself
            k1 = delta * self.funct(x_vector[ind - 1], y_vector[ind - 1])
            k2 = delta * self.funct(x_vector[ind - 1] + delta / 2, y_vector[ind - 1] + k1 / 2)
            y_vector[ind] = y_vector[ind - 1] + k2
            i += delta
            ind += 1
        return x_vector, y_vector


    # Building the function from the exact solution
    def exact_fill(self, x_vector, y_vector, delta, limit):
        i = x_vector[0] + delta
        ind = 1
        c = self.calculate_c(x_vector[0], y_vector[0])
        while i <= limit:
            x_vector[ind] = i
            y_vector[ind] = self.exact(x_vector[ind], c)
            i += delta
            ind += 1
        return x_vector, y_vector


    # The main method, computing the equation with all 3 methods (+exact)
    def compute(self, delta, IVPx, IVPy, limit):
        if delta <= 0.22222:  # the error in computing size of array appears at about 0.222(2) point.
            size_error = 0  # So this trick allows to use any step up to 10^(-5)
        else:
            size_error = 1

        # Filling the arrays with 0 initially
        euler_x_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))
        euler_y_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))
        imp_euler_x_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))
        imp_euler_y_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))
        rk_x_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))
        rk_y_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))
        exact_x_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))
        exact_y_vector = [0] * int(int(limit / delta) + size_error - int(IVPx / delta))

        # Assigning the IVPs as the first elements of X array and Y array.
        euler_x_vector[0] = imp_euler_x_vector[0] = rk_x_vector[0] = exact_x_vector[0] = IVPx
        euler_y_vector[0] = imp_euler_y_vector[0] = rk_y_vector[0] = exact_y_vector[0] = IVPy

        # Computing with each of the methods and getting X array and Y array for every method
        euler_x_vector, euler_y_vector = self.euler(euler_x_vector, euler_y_vector, delta, limit)
        imp_euler_x_vector, imp_euler_y_vector = self.improved_euler(imp_euler_x_vector, imp_euler_y_vector, delta, limit)
        rk_x_vector, rk_y_vector = self.runge_kutta(rk_x_vector, rk_y_vector, delta, limit)
        exact_x_vector, exact_y_vector = self.exact_fill(exact_x_vector, exact_y_vector, delta, limit)

        return euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector, \
               rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector


    def get_local_errors(self, euler_x_vector, euler_y_vector, imp_euler_x_vector, imp_euler_y_vector,
                         rk_x_vector, rk_y_vector, exact_x_vector, exact_y_vector):
        euler_error_vector = [0] * len(euler_y_vector)
        imp_euler_error_vector = [0] * len(imp_euler_y_vector)
        rk_error_vector = [0] * len(rk_y_vector)

        for i in range(len(euler_error_vector)):
            euler_error_vector[i] = abs(exact_y_vector[i] - euler_y_vector[i])
            imp_euler_error_vector[i] = abs(exact_y_vector[i] - imp_euler_y_vector[i])
            rk_error_vector[i] = abs(exact_y_vector[i] - rk_y_vector[i])

        return euler_error_vector, imp_euler_error_vector, rk_error_vector