def is_positive(numero):
    return numero > 0


def test_is_positive():
    assert is_positive(1) is True
    assert is_positive(2) is True
    assert is_positive(3) is True
    assert is_positive(4) is True
    assert is_positive(5) is True
    
def test_is_negative() :
    assert is_positive(0) is False
    assert is_positive(-2) is False
    
    