import pytest
from src.functions.basic_functions  import fatorial

@pytest.mark.parametrize("number", [2,3,4,5,6,7,8,9,10])
def test_fatorial_greater_than_zero(number):
    assert fatorial(number) > 1


@pytest.mark.parametrize("argument", ["5","a",-5,2.2])
def test_fatorial_invalid_type_error(argument):
    with pytest.raises(TypeError):
        fatorial(argument)

    
def test_fatorial_zero():
    assert fatorial(0) == 1