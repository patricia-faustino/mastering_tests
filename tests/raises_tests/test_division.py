import pytest
from src.funcoes import division_with_treatment


def test_division_with_treatment_with_error():
    with pytest.raises(ZeroDivisionError):
        division_with_treatment(10, 0)
        
        
def test_division_with_treatment_verify_message_error():
    with pytest.raises(ZeroDivisionError) as message_error:
        division_with_treatment(10, 0)
    assert "Division by zero is not allowed" in str(message_error)