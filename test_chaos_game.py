import pytest
import chaos_game as c


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


def test_show():
    with pytest.raises(AttributeError):
        i = c.ChaosGame(3, 1 / 2)
        i.show()