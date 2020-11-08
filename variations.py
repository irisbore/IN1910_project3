import numpy as np
import matplotlib.pyplot as plt
import triangle
import chaos_game


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

    @classmethod
    def from_chaos_game(self, chaos_instance, method):
        chaos_instance.iterate(10000)
        tx = np.take(chaos_instance.points, 0, axis=1)
        ty = np.take(chaos_instance.points, 1, axis=1)
        t = Variations(tx, ty, method)
        t.transform()
        return t


def linear_combination_wrap(var1, var2, w=0.5):
    assert 0.0 <= w <= 1.0
    x = w * var1.x + (1 - w) * var2.x
    y = w * var1.y + (1 - w) * var2.y
    result = Variations(x, y, "linear")
    result.plot()
    plt.show()


def plot_transformations_triangle():
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


def plot_transformations_chaos_game():
    c = chaos_game.ChaosGame(4, 1 / 3)
    linear = Variations.from_chaos_game(c, "linear")
    handkerchief = Variations.from_chaos_game(c, "handkerchief")
    swirl = Variations.from_chaos_game(c, "swirl")
    disc = Variations.from_chaos_game(c, "disc")

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle("transformations on chaos game")

    ax1.scatter(linear.x, -linear.y, s=0.1, color="blue")
    ax2.scatter(handkerchief.x, -handkerchief.y, s=0.1, color="teal")
    ax3.scatter(swirl.x, -swirl.y, s=0.1, color="orange")
    ax4.scatter(disc.x, -disc.y, s=0.1, c="purple")

    plt.show()


if __name__ == "__main__":
    # plot_transformations_triangle()
    # transform_grid()
    # plot_transformations_chaos_game()
    c = chaos_game.ChaosGame(3, 1 / 2)
    swirl = Variations.from_chaos_game(c, "swirl")
    disc = Variations.from_chaos_game(c, "eyefish")
    linear_combination_wrap(swirl, disc, w=0)
