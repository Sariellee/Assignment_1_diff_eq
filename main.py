import math
import matplotlib.pyplot as pyplot


def funct(x, y):
    return pow(y, 4) * math.cos(x) + y * math.tan(x)


def exact(x):
    return pow(1 / (-3 * math.tan(x) * pow(math.cos(x), -3) + pow(math.cos(x), -3)), 1 / 3)


def euler(x_vector, y_vector, delta, limit):
    i = 1
    while i < limit:
        x_vector[i] = i
        y_vector[i] = y_vector[i - 1] + delta * (funct(x_vector[i - 1], y_vector[i - 1]))
        i += delta
    return x_vector, y_vector


def improved_euler(x_vector, y_vector, delta, limit):
    i = 0
    while i < limit:
        x_vector[i] = i
        k = y_vector[i] + delta * funct(x_vector[i], y_vector[i])
        y_vector[i+1] = y_vector[i] + delta/2*(funct(x_vector[i], y_vector[i]) + funct(x_vector[i+1], k))
        i += delta
    return x_vector, y_vector


def runge_kutta(x_vector, y_vector, delta, limit):
    i = 0
    while i < limit:
        k1 = delta * funct(x_vector[i], y_vector[i])
        k2 = delta * funct(x_vector[i] + 1/2*delta, y_vector[i] + 1/2*k1)
        y_vector[i+1] = y_vector[i] + k2
        i += delta
    return x_vector, y_vector


delta = 0.5
limit = 7

x_vector = {}
y_vector = {}

i = 0
while i < limit:
    x_vector[i] = 0
    y_vector[i] = 0
    i += delta


x_vector[0] = 0
y_vector[0] = 1

x_vector, y_vector = euler(x_vector, y_vector, delta, limit)

print x_vector
print y_vector

pyplot.plot(x_vector, y_vector)
