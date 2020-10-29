import numpy as np
import matplotlib.pyplot as plt

corners = np.array([(0, 0), (1, 0), (0.5, np.sqrt(3 / 4))])
plt.scatter(*zip(*corners))
# plt.show()
# plt.figure()

weights = np.zeros(3)
points = []


def get_random_point():
    weights = np.array([np.random.random(), np.random.random(), np.random.random()])
    # weights[0] = np.random.random()
    # weights[1] = np.random.random()
    # weights[2] = np.random.random()
    weights = weights / np.sum(weights)
    return weights[1] * corners[1] + weights[2] * corners[2]


def generate_points():
    for _ in range(1000):
        points.append(get_random_point())
    plt.scatter(*zip(*points))
    plt.show()


def iterate_corners():
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

    plt.scatter(*zip(*points))
    plt.show()


iterate_corners()