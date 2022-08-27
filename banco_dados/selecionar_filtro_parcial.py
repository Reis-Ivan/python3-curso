'''Filtar linhas #2'''
# pylint: disable=E0611, C0103
from db import nova_conexao

sql = 'SELECT * FROM contatos WHERE nome like "%j%"'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    for x in cursor:
        print(x)
