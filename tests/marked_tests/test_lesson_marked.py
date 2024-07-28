import pytest
from src.functions.classify_age import classify_age

@pytest.mark.child
def test_classify_age_to_children():
    assert classify_age(10) == "Criança"

@pytest.mark.teenager
def test_classify_age_to_teenager():
    assert classify_age(14) == "Adolescente"

@pytest.mark.adult
def test_classify_age_to_adult():
    assert classify_age(59) == "Adulto"

@pytest.mark.elderly
def test_classify_age_to_elderly():
    assert classify_age(60) == "Idoso"