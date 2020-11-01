import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    def __init__(self, n, r):
        assert isinstance(n, int), "n has to be an integer"
        assert isinstance(r, float), "r has to be a float"
        assert n > 2, "n must be larger than two"
        assert 0 < r < 1, "radius needs to be between 0 and 1"
        self.n = n
        self.r = r
        # kanskje raise mer error her



p = ChaosGame(3, 0.5)


def _generate_ngon(n):
    t = np.linspace(0, 2 * np.pi, n + 1)
    c = np.zeros((n, 2))
    for i in range(n):
        c[i] = (np.sin(t[i]), np.cos(t[i]))

    return c


def plot_ngon(c):
    plt.scatter(*zip(*c), s=1, c="red")
    plt.show()

def _starting_point():
    pass

plot_ngon(_generate_ngon(16))