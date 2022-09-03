import pytest
from src.hello_world import adder

def test_adder():
    assert 5 == adder(4)
