import pytest
import math

def test_square_positve():
  assert math.pow(4,2) == 16
  
def test_square_negative():
  assert math.pow(-4,2) == 16
  
def test_square_zero():
  assert math.pow(0,2) == 0

def test_thi_one_fails():
  assert False
  
def test_always_pass():
  assert True
