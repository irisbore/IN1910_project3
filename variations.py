import numpy as np


class Variations:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

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
    def tangen(x, y):
        return (np.sin(x) / np.cos(y), np.tan(y))

    @staticmethod
    def cross(x, y):
        return np.sqrt(1 / (x ** 2 - y ** 2) ** 2) * (x, y)
