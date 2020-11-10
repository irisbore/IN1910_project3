import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        """
        Returns the point resulting from the transform

        ...
        Parameters
        ----------
        x : int or float
        y : int or float
            point

        Returns
        -------
        float
        """
        M = np.matrix([[self.a, self.b], [self.c, self.d]])
        X = np.matrix([[x, y]]).T
        c = np.matrix([self.e, self.f]).T
        a = M @ X + c
        a = [float(a[0][0]), float(a[1][0])]
        return a


def scale(probs):
    assert sum(probs) == 1, "sum of input must be 1"
    for i in range(1, len(probs)):
        probs[i] = probs[i] + probs[i - 1]
    return probs


def cumulative(f1, f2, f3, f4):
    """
    Draws function at random

    ...
    Parameters
    ----------
    f1 : object
    f2 : object
    f3 : object
    f4 : object

    Returns
    -------
    object
    """
    probs = scale([0.01, 0.85, 0.07, 0.07])
    functions = [f1, f2, f3, f4]
    r = np.random.random()
    for j, p in enumerate(probs):
        if r < p:
            return functions[j]


def iterate(f1, f2, f3, f4):
    """
    iterate new points by first picking function at random, then computing

    ...
    Parameters
    ----------
    f1 : object
    f2 : object
    f3 : object
    f4 : object

    Returns
    -------
    list
        generated points

    """
    x0 = [0, 0]
    x = [x0]
    for i in range(50000):
        f = cumulative(f1, f2, f3, f4)
        x.append(f(x[-1][0], x[-1][1]))
    return x


def plot(f1, f2, f3, f4):
    x = iterate(f1, f2, f3, f4)
    plt.scatter(*zip(*x), c="forestgreen", s=0.1)
    plt.axis("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig("barnsley_fern.png")


if __name__ == "__main__":
    f1 = AffineTransform(d=0.16)
    f2 = AffineTransform(a=0.85, b=0.04, c=-0.04, d=0.85, f=1.60)
    f3 = AffineTransform(a=0.2, b=-0.26, c=0.23, d=0.22, f=1.60)
    f4 = AffineTransform(a=-0.15, b=0.28, c=0.26, d=0.24, f=0.44)
    plot(f1, f2, f3, f4)
