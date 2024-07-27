from src.funcoes import sum_numbers
import pytest

@pytest.mark.parametrize("a,b,expected",[
    (1,2,3),(10,20,30),(15,7,22),(14,28,42)])
def test_sum(a,b,expected):
    assert sum_numbers(a,b) == expected
    
@pytest.mark.parametrize("a,b,not_expected",[
    (1,2,4),(10,20,40),(15,7,23),(14,28,45)])
def test_sum_invalid(a,b,not_expected):
    assert sum_numbers(a,b) != not_expected