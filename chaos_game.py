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
        self.c = _generate_ngon(n)
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
    random_angle = np.random.random() * 2 * np.pi
    random_x = np.random.choice((-1, 1)) * (abs(np.sin(random_angle)) - 0.5)
    random_y = np.random.choice((-1, 1)) * (abs(np.cos(random_angle)) - 0.5)

    return (random_x, random_y)


# points = np.zeros((1000, 2))

# print(points)
# for i in range(1000):
#     points[i] = _starting_point()

# plt.scatter(*zip(*points))
# plt.show()


def iterate(steps, discard=5):
    x_i = _starting_point()
    for i in range(discard):
        c_j = np.random.choice(self.c)
        x_i = self.r * x_i + (1 - self.r) * c_j


# plot_ngon(_generate_ngon(16))