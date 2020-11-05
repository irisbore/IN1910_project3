import numpy as np
import sympy as sp


class AffineTransform:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        print("in call")
        M = np.matrix([[self.a, self.b], [self.c, self.d]])
        X = np.matrix([x, y]).T
        c = np.matrix([self.e, self.f]).T
        return M @ X + c

    def cumulative(self):
        functions = [f1,f2,f3,f4]
        probs = [0.01, 0.85, 0.07, 0.07]
        probs = probs / sum(probs)
        r = np.random.random()
        for j, p in enumerate(probs):
            if r < p:
        return functions[j]



if __name__ == "__main__":
    f1 = AffineTransform(d=0.16)
    f2 = AffineTransform(a=0.85, b=0.04, c=-0.04, d=0.85, f=1.60)
    f3 = AffineTransform(a=0.2, b=-0.26, c=0.23, d=0.22, f=1.60)
    f4 = AffineTransform(a=-0.15, b=0.28, c=0.26, d=0.24, f=0.44)
