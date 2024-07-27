import pytest
from src.verify_age import verify_age


def test_verify_age_with_error():
    with pytest.raises(ValueError):
        verify_age(17)
        
def test_verify_age_without_error():
    assert verify_age(18) == "Allowed Access"