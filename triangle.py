import numpy as np
import matplotlib.pyplot as plt

corners = np.array([(0, 0), (1, 0), (0.5, np.sqrt(3 / 4))])

plt.scatter(*zip(*corners))
# plt.show()
# plt.figure()

weights = np.zeros(3)
points = []


def get_random_point():
    """
    Assigns each weight a random value between 0 and 1.
    Scales the list of weights so that the sum is 1.
    Returns a point inside the triangle expressed as a linear combination

    weights: array_like, (float, float, float, float)
        Output

        ----------
    """
    weights = np.array([np.random.random(), np.random.random(), np.random.random()])
    weights = weights / np.sum(weights)
    return weights[1] * corners[1] + weights[2] * corners[2]


def draw_points():
    """
    Docstring
    """
    for _ in range(1000):
        points.append(get_random_point())
    plt.scatter(*zip(*points))
    plt.show()


def iterate_corners():
    """
    Docstring
    """
    points = []
    x_i = get_random_point()
    random_corner = np.random.randint(0, 3)

    for i in range(5):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2

    for i in range(10000):
        random_corner = np.random.randint(0, 3)
        x_i = (x_i + corners[random_corner]) / 2
        points.append(x_i)

    plt.scatter(*zip(*points), s=0.1, marker=".")
    plt.axis("equal")
    plt.show()


iterate_corners()
