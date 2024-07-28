from src.functions.basic_functions  import double_sum
import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

def test_double_sum(numbers):
    assert double_sum(numbers) == 30
    
def test_empty_list_double_sum():
    assert double_sum([]) == 0