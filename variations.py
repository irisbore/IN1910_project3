import numpy as np
import matplotlib.pyplot as plt
import triangle


class Variations:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self._func = getattr(Variations, name)

    def transform(self):
        self.x, self.y = self._func(self.x, self.y)
        return self.x, self.y

    def plot(self, cmap="jet"):
        plt.scatter(self.x, self.y, cmap=cmap)

    @staticmethod
    def linear(x, y):
        return x, y

    @staticmethod
    def handkerchief(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan(x, y)
        return r * (np.sin(theta + r), np.cos(theta - r))

    @staticmethod
    def swirl(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        return (
            x * np.sin(r ** 2) - y * np.cos(r ** 2),
            x * np.cos(r ** 2) + y * np.sin(r ** 2),
        )

    @staticmethod
    def disc(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan(x, y)
        return theta / np.pi * (np.sin(np.pi * r), np.cos(np.pi * r))

    @staticmethod
    def fisheye(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        return 2 / (r + 1) * (y, x)

    @staticmethod
    def eyefish(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        return 2 / (r + 1) * (x, y)

    @staticmethod
    def tangent(x, y):
        return (np.sin(x) / np.cos(y), np.tan(y))

    @staticmethod
    def cross(x, y):
        return np.sqrt(1 / (x ** 2 - y ** 2) ** 2) * (x, y)


def plot_2_transformations_triangle():
    points, _ = triangle.iterate_corners()
    swirl = Variations(points[:, 0], points[:, 1], "swirl")
    swirl.transform()

    eyefish = Variations(points[:, 0], points[:, 1], "eyefish")
    eyefish.transform()

    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle("two transformations")

    ax1.scatter(swirl.x, swirl.y, c="orange")
    ax1.set_ylabel("swirl")

    ax2.scatter(eyefish.x, eyefish.y, c="purple")
    ax2.set_ylabel("eyefish")


def transform_grid():
    N = 80
    grid_values = np.linspace(-1, 1, N)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()

    transformations = ["linear", "handkerchief", "swirl", "disc"]
    variations = [
        Variations(x_values, y_values, version) for version in transformations
    ]

    fig, axs = plt.subplots(2, 2, figsize=(9, 9))
    for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):

        u, v = variation.transform()

        ax.plot(
            u,
            -v,
            markersize=1,
            marker=".",
            linestyle="",
            color=[np.random.random(), np.random.random(), np.random.random()],
        )
        # ax.scatter(u, -v, s=0.2, marker=".", color="black")
        ax.set_title(variation.name)
        ax.axis("off")

    # fig.savefig("figures/variations_4b.png")
    plt.show()


if __name__ == "__main__":
    plot_2_transformations_triangle()
    transform_grid()
