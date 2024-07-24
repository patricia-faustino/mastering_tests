import pytest

## escopo padrão não precisaria definir
@pytest.fixture(scope="function")
def fixture_function():
    return 10

@pytest.fixture(scope="module")
def fixture_module():
    return 20

@pytest.fixture(scope="session")
def fixture_session():
    return 30

def test_fixture_function(fixture_function):
    assert fixture_function == 10
    
def test_fixture_function_retentative(fixture_function):
    assert fixture_function == 10
    
def test_fixture_function_module(fixture_function, fixture_module):
    assert fixture_function == 10
    assert fixture_module == 20


def test_fixture_function_module_retentative(fixture_module):
    assert fixture_module == 20


def test_fixture_function_module_session(fixture_session):
    assert fixture_session == 30