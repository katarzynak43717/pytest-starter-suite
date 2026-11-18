import pytest

@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (-1, 1, 0), (0, 0, 0)])
def test_addition(a, b, expected):
    assert a + b == expected
