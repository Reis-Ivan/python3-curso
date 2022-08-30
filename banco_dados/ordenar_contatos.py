'''Seleção de dados'''
# pylint: disable=E0611, C0103
from db import nova_conexao

sql = 'SELECT nome, id from contatos ORDER BY nome DESC'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    print('\n'.join(str(registro) for registro in cursor))
    