import pytest
import time
from src.funcoes import slow_sum, multiply

@pytest.mark.slow
def test_slow_sum():
    assert slow_sum(1,2) == 3

@pytest.mark.flash
def test_flash_sum():
    assert sum([1,2]) == 3
    
@pytest.mark.slow
def test_flash_multiply():
    time.sleep(3)
    assert multiply(2,3) == 6