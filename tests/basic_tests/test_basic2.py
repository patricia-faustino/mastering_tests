def sum(a, b):
    return a + b

def length(list):
    return len(list)

## seguindo as boas práticas de código esse comportamento não é adequado
## cada teste deve validar somente um comportamento
def test_sum_e_comprimento():
    assert sum(3, 2) == 5
    assert length([1,2,3,4,5]) == 5