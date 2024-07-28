from src.functions.basic_functions import *

def test_email_is_valid():
    assert email_is_valid("exemplo@dominio.com") is True
    
def test_email_is_invalid():
    assert email_is_valid("exemplodominio.com") is False
    assert email_is_valid("exemplo@dominiocom") is False
    assert email_is_valid("") is False
    
    
def test_divide():
    assert divide(4,2) == 2
    assert divide(4,0) is None