import pytest
from src.functions.basic_functions import slow_sum

## Comandos para executar os testes marcados
## python -m pytest -m slow 
## python -m pytest -m "not slow"   
## python -m pytest -m "slow and flash"
## python -m pytest -m "slow or flash"
## python -m pytest -m "slow or not flash"  
## não lista teste que estão fora do resultado da expressão(- k): 
## python -m pytest -k "slow" 

@pytest.mark.slow
@pytest.mark.flash
def test_slow_and_flash():
    assert slow_sum(1,2) == 3
    
    
@pytest.mark.slow
def test_slow_multiple_marked():
    assert slow_sum(1,4) == 5

@pytest.mark.flash
def test_flash_multiple_marked():
    assert sum([1,4]) == 5

