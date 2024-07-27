import pytest
from src.calculate_total import calculate_total

@pytest.mark.parametrize("price", [100, 200,300,400])
@pytest.mark.parametrize("discount_rate", [0, 0.1, 0.2, 0.5])
@pytest.mark.parametrize("tax_rate", [0.05, 0.03, 0.04])
def test_calculate_total(price, discount_rate, tax_rate):
    expected_discount = price * discount_rate
    expected_tax = (price - expected_discount) * tax_rate
    expected_total = price - expected_discount + expected_tax
    assert calculate_total(price, discount_rate, tax_rate) == expected_total