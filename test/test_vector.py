import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from src.vector import Vector


def test_init_incorrect_value():
    with pytest.raises(TypeError):
        Vector("1", 2, 3)
    with pytest.raises(TypeError):
        Vector(1, "2", 3)
    with pytest.raises(TypeError):
        Vector(1, 2, "3")
    with pytest.raises(TypeError):
        Vector(True, 2, 3)
    with pytest.raises(TypeError):
        Vector(1, True, 3)
    with pytest.raises(TypeError):
        Vector(2, 2, True)


class TestAdd:
    def test_add_vector_positive_values(self):
        a = Vector(1, 2, 3)
        b = Vector(3, 5, 9)
        c = a + b
        result = Vector(4, 7, 12)
        assert result == c

    def test_add_vector_negative_values(self):
        a = Vector(-1, -2, -3)
        b = Vector(-1, -3, -2)
        c = a + b
        result = Vector(-2, -5, -5)
        assert result == c

    def test_add_vector_mixed_values(self):
        a = Vector(1, -2, 0)
        b = Vector(-3, 0, 2)
        c = a + b
        result = Vector(-2, -2, 2)
        assert result == c


class TestSub:
    def test_sub_positive_values(self):
        a = Vector(1, 2, 3)
        b = Vector(1, 3, 2)
        c = a - b
        result = Vector(0, -1, 1)
        assert result == c

    def test_sub_negative_values(self):
        a = Vector(-1, -2, -3)
        b = Vector(-1, -3, -2)
        c = a - b
        result = Vector(0, 1, -1)
        assert result == c

    def test_sub_mixed_values(self):
        a = Vector(1, -2, 0)
        b = Vector(-3, 0, 2)
        c = a - b
        result = Vector(4, -2, -2)
        assert result == c


# Test multiplication
class TestMul:
    def test_mul_vectors_positive_values(self):
        a = Vector(1, 2, 3)
        b = Vector(3, 1, 2)
        c = a * b
        result = 11
        assert result == c

    def test_mul_vectors_negative_values(self):
        a = Vector(-1, -2, -3)
        b = Vector(-3, -1, -2)
        c = a * b
        result = 11
        assert result == c

    def test_mul_vectors_mixed_values(self):
        a = Vector(-1, 2, 3)
        b = Vector(3, -1, 2)
        c = a * b
        result = 1
        assert result == c

    def test_mul_number_positive_value(self):
        a = Vector(1, 2, -3)
        c = a * 2
        result = Vector(2, 4, -6)
        assert result == c


class TestAngel:
    def test_angel_positive_values(self):
        a = Vector(0, 1, 0)
        b = Vector(1, 0, 0)
        c = a.angel(b)
        assert c == 90
        b = Vector(1, 1, 0)
        c = a.angel(b)
        assert c == 45
        b = Vector(0, -1, 0)
        c = a.angel(b)
        assert c == 180
        b = Vector(1, -1, 0)
        c = a.angel(b)
        assert c == 135


def test_vector_str_output():
    a = Vector(-1, 2, 3.5)
    assert str(a) == "(-1|2|3.5)"


def test_cross_product_positive_values():
    a = Vector(1, 2, 3)
    b = Vector(3, 2, 1)
    c = a.cross_product(b)
    assert a * c == 0
    assert b * c == 0
