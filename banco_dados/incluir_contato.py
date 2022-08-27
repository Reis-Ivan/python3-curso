'''Inclusão de dados'''
# pylint: disable=E0611, C0103

from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Lucas', '98765-4321')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Errp: {e.msg}')
    else:
        print('1 registro incluido, ID:', cursor.lastrowid)
        