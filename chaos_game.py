import numpy as np


class ChaosGame:
    def __init__(self, n, r):
        assert isinstance(n, int), "n has to be an integer"
        assert isinstance(r, float), "r has to be a float"
        assert n > 2, "n must be larger than two"
        assert 0 < r < 1, "radius needs to be between 0 and 1"
        self.n = n
        self.r = r
        # kanskje raise mer error her


p = ChaosGame(3, 0.5)


def _generate_ngon(n):
    pass
