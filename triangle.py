import numpy as np
import matplotlib.pyplot as plt

corners = np.array([(0, 0), (1, 0), (0.5, np.sqrt(3 / 4))])
plt.scatter(*zip(*corners))
# plt.show()
# plt.figure()


def get_random_point():
    """
    Assigns each weight a random value between 0 and 1.
    Scales the list of weights so that the sum is 1.
    Returns a point inside the triangle expressed as a linear combination

    weights: array_like, (float, float, float, float)
        Output

        ----------
    """
    weights = np.zeros(3)
    weights = np.array([np.random.random(), np.random.random(), np.random.random()])
    weights = weights / np.sum(weights)
    return weights[1] * corners[1] + weights[2] * corners[2]


def draw_points():
    """
    Docstring
    """
    points = []
    for _ in range(1000):
        points.append(get_random_point())
    plt.scatter(*zip(*points))
    plt.show()


# draw_points()


def iterate_corners():
    """
    Docstring
    """
    points = []
    colors = np.zeros(10000)
    x_i = get_random_point()
    random_corner = np.random.randint(0, 3)

    for i in range(5):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2

    for i in range(10000):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2
        points.append(x_i)
        colors[i] = random_corner

    return points, colors


def plot_points(points):
    plt.scatter(*zip(*points), s=0.1, marker=".")
    plt.axis("equal")
    plt.show()


def alt_iterate():
    points, colors = iterate_corners()
    n = len(colors)
    # red = X[colors == 0]
    # green = X[colors == 1]
    # blue = X[colors == 2]
    color = "b"
    for i in range(n):
        if colors[i] == 0:
            plt.scatter(points[i][0], points[i][1], color="r")
        elif colors[i] == 1:
            plt.scatter(points[i][0], points[i][1], color="g")
        else:
            plt.scatter(points[i][0], points[i][1], color="b")
    plt.show()


def color_iterate():
    points, colors = iterate_corners()
    colors_value = []

    for i in range(len(colors)):
        if colors[i] == 0:
            colors_value.append("red")
        elif colors[i] == 1:
            colors_value.append("green")
        else:
            colors_value.append("blue")

    # plt.scatter(red, color="r")
    # plt.scatter(green, color="green")
    # plt.scatter(blue, color="blue")
    plt.scatter(*zip(*points), s=0.1, c=colors_value, marker=".")
    plt.show()


color_iterate()
