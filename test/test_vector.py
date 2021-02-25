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
