import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from src.vector import Vector


def test_add_vector_positive_values():
    a = Vector(1, 2, 3)
    b = Vector(3, 5, 9)
    c = a + b
    result = Vector(4, 7, 12)
    assert result == c


def test_add_vector_negative_values():
    a = Vector(-1, -2, -3)
    b = Vector(-1, -3, -2)
    c = a + b
    result = Vector(-2, -5, -5)
    assert result == c


def test_add_vector_mixed_values():
    a = Vector(1, -2, 0)
    b = Vector(-3, 0, 2)
    c = a + b
    result = Vector(-2, -2, 2)
    assert result == c


def test_vector_str_output():
    a = Vector(-1, 2, 3.5)
    assert str(a) == "(-1|2|3.5)"
