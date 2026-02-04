from calculator import add, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_larger_numbers():
    assert add(10, 20) == 30


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_mixed_numbers():
    assert add(-5, 10) == 5


def test_add_zeros():
    assert add(0, 0) == 0


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_larger_second_number():
    assert subtract(10, 20) == -10


def test_subtract_zeros():
    assert subtract(0, 0) == 0


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2
