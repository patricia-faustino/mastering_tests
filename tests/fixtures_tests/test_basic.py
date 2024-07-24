import pytest

@pytest.fixture
def sample_list():
    return [1,2,3,4,5]

def test_sum(sample_list):
    assert sum(sample_list) == 15
    
def test_length(sample_list):
    assert len(sample_list) == 5
    
def test_result_list(sample_list):
    expected_list = [1,2,3,4,5]
    result_list = sample_list
    assert result_list == expected_list
    
def test_first_element(sample_list):
    assert sample_list[0] == 1