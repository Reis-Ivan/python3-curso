'''Incluir Casa e trabalho'''
# pylint: disable=E0611, C0103

from mysql.connector.errors import ProgrammingError
from db import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contatos = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    'Ana': 'Casa',
    'Bia': 'Trabalho',
    'Luca':'Casa',
    'Lucio':'Trabalho',
    'Beca':'Casa',
    'Pedro':'Trabalho',
    'Doug':'Casa',
    'Jana':'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo,(grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contatos, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos associados')
