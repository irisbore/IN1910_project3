import pytest
import chaos_game as c


"""Check if distance from starting points to every single corner doesn't exceed some distance """

"""
def test_starting_point():
    # Starting point
    X0 = starting_point()
    x0 = X0[0]
    y0 = X0[1]
    for n in range(10):
        corners = c.corners(n)
        for i in range(len(corners)):
            result = (y0 - corners[0][1]) * (corners[1][0] - corners[0][0]) - (
                x0 - corners[0][0]
            ) * (corners[1][1] - corners[0][1])
            if result=0:
                print(point lies on the line)
"""


def test_assert_type():
    with pytest.raises(AssertionError):
        u = c.ChaosGame(2.2, 0.5)
        v = c.ChaosGame(4, 2)


def test_assert_value():
    with pytest.raises(AssertionError):
        u = c.ChaosGame(3.2, 0.5)
        v = c.ChaosGame(4, 1)


def test_savepng():
    i = c.ChaosGame(4, 0.5)
    with pytest.raises(NameError):
        i.savepng(outfile.pdf)


"""Check if _generate_ngon(n) is in __init__"""


def test_init():
    pass
