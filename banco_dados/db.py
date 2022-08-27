'''Função nova conexão'''
from contextlib import contextmanager
from mysql.connector import connect

parametros = dict (
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'Ivan@232765',
    database = 'agenda'
)

@contextmanager
def nova_conexao():
    '''Função que cria conexão'''
    conexao = connect (**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
            