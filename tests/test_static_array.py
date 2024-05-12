import pytest
import arrays.static_array as sa


@pytest.fixture
def sa1():
    return sa.StaticArr()


def test_init(sa1):
    # Check sa1
    placeholder_check1 = True
    count_check1 = 0
    for el in sa1._array:
        count_check1 += 1
        if el != sa1._placeholder:
            placeholder_check1 = False

    # Assertions sa1
    assert sa1.allocation_size == 8
    assert placeholder_check1
    assert count_check1 == sa1.allocation_size
    assert sa1._end_point == -1


def test_size(sa1):
    assert sa1.size() == 0


def test_append(sa1):
    """
    1. _end_point is incremented as expected up til end
    2. size() is what we expect after each append
    3. If we append too much the error is thrown
    4. Check that the list is what we think it should be
    """
    # 1st
    sa1.append(0)
    assert sa1._end_point == 0
    assert sa1.size() == 1

    # 2nd
    sa1.append(1)
    assert sa1._end_point == 1
    assert sa1.size() == 2

    # 3rd
    sa1.append(2)
    assert sa1._end_point == 2
    assert sa1.size() == 3

    # 4th 5th 6th 7th 8th
    sa1.append(3)
    sa1.append(3)
    sa1.append(3)
    sa1.append(3)
    sa1.append(3)

    assert sa1._end_point == 7
    assert sa1.size() == 8

    # Test the IndexError
    with pytest.raises(IndexError):
        sa1.append(3)


def test_insert(sa1):
    # Test that we can't insert further than the _end_point + 1
    with pytest.raises(IndexError):
        sa1.insert(2, 0)

    # Test that insertions generally work
    sa1.insert(0, 0)
    assert sa1.size() == 1
    assert sa1.get(0) == 0

    sa1.insert(0, 1)
    assert sa1.size() == 2
    assert sa1.get(1) == 1

    sa1.insert(0, 2)
    assert sa1.size() == 3
    assert sa1.get(2) == 2

    sa1.insert(0, 3)
    assert sa1.size() == 4
    assert sa1.get(3) == 3
