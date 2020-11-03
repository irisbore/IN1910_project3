import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class ChaosGame:
    def __init__(self, n, r=1 / 2):
        assert isinstance(n, int), "n has to be an integer"
        assert isinstance(r, float), "r has to be a float"
        assert n > 2, "n must be larger than two"
        assert 0 < r < 1, "radius needs to be between 0 and 1"
        self.n = n
        self.r = r
        _generate_ngon()
        # kanskje raise mer error her

    def __call__(self):
        pass

    def _generate_ngon(self, n):
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
        self.corners = [(np.sin(angle), np.cos(angle)) for angle in angles]

    def plot_ngon(self):
        plt.scatter(*zip(*self.corners), s=1, c="red")
        plt.show()

    def _starting_point(self):
        random_angle = np.random.random(self.n)
        random_angle = random_angle / np.sum(random_angle)
        random_x = np.random.choice((-1, 1)) * (abs(np.sin(random_angle)) - self.r)
        random_y = np.random.choice((-1, 1)) * (abs(np.cos(random_angle)) - self.r)
        return (random_x, random_y)

    def iterate(self, steps, discard=5):
        x_i = self._starting_point()
        points = []
        indices = []
        for i in range(discard):
            index = np.random.randint(self.n)
            x_i = self.r * x_i + (1 - self.r) * self.corners[index]
        for i in range(steps):
            index = np.random.randint(self.n)
            c_j = np.random.choice(self.corners)
            x_i = self.r * x_i + (1 - self.r) * self.corners[index]
            points.append(x_i)
            indices.append(index)

            # evt bruk "jet" for cmap

    def plot(color=False, cmap="BrBG"):
        return 0

    # Lag property @

    def savepng(outfile, color=False, cmap="jet"):
        # plt.savefig()
        return 0


if __name__ == "__main__":
    c = ChaosGame(5)
    c._starting_point()
    c.iterate(1)
    # points = np.zeros((1000, 2))

    # for i in range(1000):
    #     points[i] = _starting_point()

    # plt.scatter(*zip(*points))
    # plt.show()
