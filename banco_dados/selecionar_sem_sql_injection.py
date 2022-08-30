'''Consulta com INPUT'''
# pylint: disable=E0611, C0103
from db import nova_conexao

sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%')
    cursor = conexao.cursor()
    cursor.execute(sql, args)
    for x in cursor:
        print(x)
