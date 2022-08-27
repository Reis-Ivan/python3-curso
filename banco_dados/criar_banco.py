'''Criação banco de dados'''

from mysql.connector import connect

conexao = connect (
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd ='Ivan@232765'
)

cursor = conexao.cursor()
# OPÇÃO: CREATE DATABASE IF NOT EXISTS agenda
cursor.execute('CREATE DATABASE agenda')
