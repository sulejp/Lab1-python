import matplotlib.pyplot as plt
import numpy as np

plt.grid()

def przyklad():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x ** 2 - 5 * x + 3)
    plt.xlabel('$x$')  # os x
    plt.ylabel('$f(x)$')  # os y
    plt.plot(x, y)  # przekazujemy zbiory wartosci
    plt.show()


def funkcja1():
    x = np.arange(-5, 5, 0.01)
    y = np.tanh(x)
    plt.xlabel('$x$')  # os x
    plt.ylabel('$f(x)$')  # os y
    plt.plot(x, y)
    plt.show()


def funkcja2():
    x = np.arange(-5, 5, 0.01)
    y = ((np.e ** x) - (np.e ** (-x))) / ((np.e ** x) + (np.e ** (-x)))
    plt.xlabel('$x$')  # os x
    plt.ylabel('$f(x)$')  # os y
    plt.plot(x, y)
    plt.show()


def funkcja3():
    x = np.arange(-5, 5, 0.01)
    y = 1 / (1 + (np.e ** (-x)))
    plt.xlabel('$x$')  # os x
    plt.ylabel('$f(x)$')  # os y
    plt.plot(x, y)
    plt.show()


def funkcja4():
    x = np.arange(-5, 5, 0.01)
    y = [0 if i <= 0 else i for i in x]
    plt.xlabel('$x$')  # os x
    plt.ylabel('$f(x)$')  # os y
    plt.plot(x, y)
    plt.show()


def funkcja5():
    x = np.arange(-5, 5, 0.01)
    y = [0 if i <= 0 else np.e ** i - 1 for i in x]
    plt.xlabel('$x$')  # os x
    plt.ylabel('$f(x)$')  # os y
    plt.plot(x, y)
    plt.show()


funkcja5()
