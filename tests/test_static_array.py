import pytest
import arrays.static_array as sa


@pytest.fixture
def sa1():
    return sa.StaticArr()


def test_initialization(sa1):
    print(sa1)
