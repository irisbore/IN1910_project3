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
    Returns a point inside the triangle expressed as a linear combination.

    weights: array_like, (float, float, float, float)
        Output

        ----------
    """
    weights = np.random.random(3)
    weights = weights / np.sum(weights)
    x_0 = weights @ corners[:, 0]
    y_0 = weights @ corners[:, 1]
    X_0 = (x_0, y_0)
    return X_0


def draw_points():
    """
    Plots 1000 random points within a triangle.
    """
    points = []
    for _ in range(1000):
        points.append(get_random_point())
    plt.scatter(*zip(*points))
    plt.show()


def iterate_corners():
    """
    Finds 10000 points within a triangle.
    Each point is selected by choosing a random corner
    and moving halfway between the old point and the corner.

    points - tupple of points with shape (10000,2)
    colors - the IDs of the corners wich were chosen to calculate the points
    with the corresponding indices.

    returns
        points, colors
    """
    points = np.zeros((10000, 2))
    colors = np.zeros(10000)
    x_i = get_random_point()
    random_corner = np.random.randint(0, 3)

    for i in range(5):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2

    for i in range(10000):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2
        points[i] = x_i
        colors[i] = random_corner

    return points, colors


def plot_points(points):
    """
    Plots the points with pyplot scatter
    Input: points - (x,y)
    """
    plt.scatter(*zip(*points), s=0.1, marker=".")
    plt.axis("equal")
    plt.show()


def color_iterate():
    points, colors = iterate_corners()

    red = points[colors == 0]
    green = points[colors == 1]
    blue = points[colors == 2]

    color_translate = {"red": red, "green": green, "blue": blue}

    plt.scatter(*zip(*red), s=0.1, c="red", marker=".")
    plt.scatter(*zip(*green), s=0.1, c="green", marker=".")
    plt.scatter(*zip(*blue), s=0.1, c="blue", marker=".")

    plt.show()


# def alt_iterate():
#     points, colors = iterate_corners()
#     n = len(colors)
#     # red = X[colors == 0]
#     # green = X[colors == 1]
#     # blue = X[colors == 2]
#     for i in range(n):
#         if colors[i] == 0:
#             plt.scatter(points[i][0], points[i][1], color="r")
#         elif colors[i] == 1:
#             plt.scatter(points[i][0], points[i][1], color="g")
#         else:
#             plt.scatter(points[i][0], points[i][1], color="b")
#     plt.show()


# def color_iterate2():
#     points, colors = iterate_corners()
#     colors_value = []

#     for i in range(len(colors)):
#         if colors[i] == 0:
#             colors_value.append("red")
#         elif colors[i] == 1:
#             colors_value.append("green")
#         else:
#             colors_value.append("blue")

#     # plot tre ganger
#     # plt.scatter(red, color="r")
#     # plt.scatter(green, color="green")
#     # plt.scatter(blue, color="blue")
#     plt.scatter(*zip(*points), s=0.1, c=colors_value, marker=".")
#     plt.show()


def alternative_colors():
    """
    Plots 1000 points inside a triangle with colors in
    a gradient between the three corners.
    """
    points = np.zeros((1000, 2))
    colors = np.zeros((1000, 3))
    corner_color = np.array([(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)])
    x_i = get_random_point()
    x_color = np.array((1.0, 1.0, 1.0))
    random_corner = np.random.randint(0, 3)

    for i in range(5):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2
        x_color = (x_color + corner_color[random_corner]) / 2

    for i in range(1000):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2
        x_color = (x_color + corner_color[random_corner]) / 2
        points[i] = x_i
        colors[i] = x_color

    for p, c in zip(points, colors):
        plt.scatter(p[0], p[1], c=c)
    plt.show()


alternative_colors()