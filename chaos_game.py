import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class ChaosGame:
    def __init__(self, n, r=1 / 2):
        """
        Calls _generate_ngon(n)

        Parameters
        ----------
        n : int
        r : float
        """
        assert isinstance(n, int), "n has to be an integer"
        assert isinstance(r, float), "r has to be a float"
        assert n > 2, "n must be larger than two"
        assert 0 < r < 1, "radius needs to be between 0 and 1"
        self.n = n
        self.r = r
        self._generate_ngon(n)

    def _generate_ngon(self, n):
        """
        Parameters
        ----------
        n : int
            number of corners in polygon
        Returns
        -------
        list
            corners

        """
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
        self.corners = np.array([(np.sin(angle), np.cos(angle)) for angle in angles])

    def plot_ngon(self):
        plt.scatter(*zip(*self.corners), s=1, c="red")
        plt.show()

    def _starting_point(self):
        """
        Parameters
        ----------
        n : int
            number of corners in polygon
        Returns
        -------
        list
            corners

        """
        weights = np.random.random(size=self.n)
        weights = weights / np.sum(weights)
        X_0 = np.zeros(2)
        X_0[0] = weights @ self.corners[:, 0]
        X_0[1] = weights @ self.corners[:, 1]
        return X_0

    def iterate(self, steps, discard=5):
        x_i = self._starting_point()
        self.points = []
        self.indices = []
        for i in range(discard):
            index = np.random.randint(self.n)
            x_i = self.r * x_i + (1 - self.r) * self.corners[index]
        for i in range(steps):
            index = np.random.randint(self.n)
            x_i = self.r * x_i + (1 - self.r) * self.corners[index]
            self.points.append(x_i)
            self.indices.append(index)

    def plot(self, color=False, cmap="jet"):
        if color == True:
            colors = self.gradient_color
        else:
            colors = "black"

        plt.scatter(*zip(*self.points), c=colors, cmap=cmap)
        plt.axis("equal")

    def show(self, color=False, cmap="jet"):
        assert getattr(self, "points"), "you need to call iterate"
        self.plot(color=color, cmap=cmap)
        # plt.show()

    @property
    def gradient_color(self):
        """Property"""
        c = [self.indices[0]]
        for i in range(1, len(self.indices)):
            c.append((c[-1] + self.indices[i]) / 2)
        return c

    def savepng(self, outfile, color=False, cmap="jet"):
        newfile = outfile.split(".")
        if len(newfile) == 1:
            outfile = f"{outfile}.png"
            plt.savefig(outfile, dpi=300)

        if outfile.endswith(".png"):
            outfile = outfile
            plt.savefig(outfile, dpi=300)
        else:
            raise NameError("Filename must be a .png ")


def save_figures():
    corners = [3, 4, 5, 5, 6]
    radii = [1 / 2, 1 / 3, 1 / 3, 3 / 8, 1 / 3]
    names = ["1", "2", "3", "4", "5"]

    for n, r, name in zip(corners, radii, names):
        c = ChaosGame(n, r)
        c.iterate(10000)
        c.show(color=True)
        c.savepng(f"figures/chaos{name}", color=True)
        plt.clf()


if __name__ == "__main__":
    pass
    # c = ChaosGame(n=3, r=1 / 2)
    # c.iterate(10000)
    # c.show(color=True)
    # c.savepng("chaos1", color=True)
    # save_figures()