'''Configuração MySQL'''
from mysql.connector import connect

conexao = connect (
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'Ivan@232765'
)

print(conexao)
