import pytest
import sqlalchemy
from sqlalchemy.sql import text

@pytest.fixture
def database_connection():
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    connection = engine.connect()
    ## setup
    yield connection
    ##teaardown
    connection.close()
    
    
def test_database_connection(database_connection):
    result = database_connection.execute(text("select 1"))
    assert result.fetchone()[0] == 1