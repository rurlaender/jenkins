import pytest
import math

def test_square_positve():
  assert math.pow(4,2) == 16
  
def test_square_negative():
  assert math.pow(-4,2) == 16
  
