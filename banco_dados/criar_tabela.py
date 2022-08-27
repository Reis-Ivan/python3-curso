'''Criação de tabela'''
# pylint: disable=E0611, C0103
from mysql.connector import ProgrammingError
from db import nova_conexao


tabela_contatos = """
    CREATE TABLE contatos (
        nome VARCHAR(50),
        tel VARCHAR(40)
    )
"""

tabale_emails = """
    CREATE TABLE emails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabale_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro externo: {e.msg}')
        