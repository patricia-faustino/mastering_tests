import pytest
from unittest.mock import Mock, patch
from src.projeto_final.database_manager import Cliente, DatabaseManager


@pytest.fixture
def build_client():
    ## nome,email,telefone,endereco,cidade,estado,cep,datacadastro,datanascimento
    client={
            'nome': 'John Doe', 
            'email': 'email',
            'telefone': '123456786',
            'endereco': 'Rua das Marcas', 
            'cidade': 'São Paulo',
            'estado': 'SP',
            'cep': '12345-678',
            'datacadastro': '2023-03-15',
            'datanascimento': '1990-01-01'
        }
    nome = client.get('nome')
    email = client.get('email@email.com')
    telefone = client.get('telefone')
    endereco = client.get('endereco')
    cidade = client.get('cidade')
    estado = client.get('estado')
    cep = client.get('cep')
    datacadastro = client.get('datacadastro')
    datanascimento = client.get('datanascimento')
    
    return Cliente(nome, email, telefone, endereco, cidade, estado, cep, datacadastro, datanascimento)
    
    
@pytest.fixture(params= [
    {'nome': 'John Doe', 'email': 'email', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023-03-15', 'datanascimento': '1990-01-01'},
    {'nome': 'Marie Doe', 'email': 'email@email.com', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023-03-15', 'datanascimento': None},
    {'nome': 'Phietro Doe', 'email': 'email@email.com', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023-03-15', 'datanascimento': '1990/01/01'},
    {'nome': 'Liniker Doe', 'email': 'email@email.com', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023/03/15', 'datanascimento': '1990-01-01'},
    ])
def build_cliente_com_parametros_nao_validos(request):
    cliente = request.param
    return Cliente(**cliente)

@pytest.fixture(params= [
    {'nome': 'John Doe', 'email': 'email@email.com', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023-03-15', 'datanascimento': '1990-01-01'},
    {'nome': 'Marie Doe', 'email': 'email@email.com', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023-03-15', 'datanascimento': '1990-01-01'},
    {'nome': 'Phietro Doe', 'email': 'email@email.com', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023-03-15', 'datanascimento': '1990-01-01'},
    {'nome': 'Liniker Doe', 'email': 'email@email.com', 'telefone': '123456786', 'endereco': 'Rua das Marcas', 'cidade': 'São Paulo', 'estado': 'SP', 'cep': '12345-678', 'datacadastro': '2023-03-15', 'datanascimento': '1990-01-01'},
    ])
def build_cliente_com_parametros_validos(request):
    cliente = request.param
    return Cliente(**cliente)
    

@pytest.fixture
def build_db_manager():
    db_manager = DatabaseManager(':memory:')  # Usando um banco de dados em memória para testes
    db_manager.create_connection()
    db_manager.criar_tabela_users()
    yield db_manager
    db_manager.fechar_conexao()

def test_incluir_cliente_deve_retornar_cliente_valido(build_cliente_com_parametros_validos, build_db_manager):
    client = build_cliente_com_parametros_validos
    
    resultado_inclusao = build_db_manager.incluir_cliente(client)
    
    assert resultado_inclusao > 0
    
    
def test_incluir_cliente_deve_retornar_id_cliente_invalido(build_cliente_com_parametros_nao_validos, build_db_manager):
    client = build_cliente_com_parametros_nao_validos
    
    resultado_inclusao = build_db_manager.incluir_cliente(client)
    
    assert resultado_inclusao == "Falha na validação dos dados do cliente."
    
    
def test_validar_cliente_return_false_quando_dado_for_invalido(build_cliente_com_parametros_nao_validos, build_db_manager):
    client_build = build_cliente_com_parametros_nao_validos
    
    assert build_db_manager.validar_cliente(client_build) == False
    
def test_validar_cliente_return_true_quando_dado_for_valido(build_cliente_com_parametros_validos, build_db_manager):
    client_build = build_cliente_com_parametros_validos
    
    assert build_db_manager.validar_cliente(client_build) == True


def test_deve_atualizar_cliente(build_cliente_com_parametros_validos, build_db_manager):
    client_build = build_cliente_com_parametros_validos
    
    resultado_inclusao = build_db_manager.incluir_cliente(client_build)
    
    campo = 'nome'
    valor = 'Mariazinha'
    
    client_atualizado = build_db_manager.atualizar_cliente(resultado_inclusao, campo, valor)
    
    assert client_atualizado > 0
    

def test_nao_deve_atualizar_cliente_com_id_invalido(build_db_manager):
    campo = 'nome'
    valor = 'Mariazinha'
    
    client_atualizado = build_db_manager.atualizar_cliente(0, campo, valor)
    
    assert client_atualizado == "ID inválido ou inexistente."