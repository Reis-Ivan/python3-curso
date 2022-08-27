"""Desafio excluir a tabela email"""
# pylint: disable=E0611, C0103
from mysql.connector.errors import ProgrammingError
from db import nova_conexao

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE emails')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
        