import pytest
from src.functions.classify_age import classify_age

@pytest.mark.parametrize("age, expected_category", [
    (0, "Criança"),
    (11, "Criança"),
    (12, "Adolescente"),
    (17, "Adolescente"),
    (18, "Adulto"),
    (59, "Adulto"),
    (60, "Idoso"),
    (100, "Idoso")
])
def test_classify_age_expected_category(age, expected_category):
    assert classify_age(age) == expected_category
    
@pytest.mark.parametrize("age, not_expected_category", [
    (0, "Adolescente"),
    (11, "Adulto"),
    (12, "Criança"),
    (17, "Criança"),
    (18, "Idoso"),
    (59, "Idoso"),
    (60, "Adulto"),
    (100, "Criança")
])
def test_classify_age_not_expected_category(age, not_expected_category):
    assert classify_age(age) != not_expected_category