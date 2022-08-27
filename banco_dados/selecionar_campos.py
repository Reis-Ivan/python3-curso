'''Inclusão de dados'''
# pylint: disable=E0611, C0103

from db import nova_conexao

sql = 'SELECT tel, nome FROM contatos'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    for contato in cursor.fetchall():
        print('\t'.join(str(campo) for campo in contato))
        