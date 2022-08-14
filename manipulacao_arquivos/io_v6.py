#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=unspecified-encoding
'''Escrevendo no arquivo'''

with open('manipulacao_arquivos/pessoas.csv',) as arquivo:
    with open('manipulacao_arquivos/pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.close:
    print('Arquivo já foi fechado!')

if saida.close:
    print('O arquivo de saída já foi fechado!')
