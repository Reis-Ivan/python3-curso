#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=unspecified-encoding
'''Bloco WITH'''

with open('manipulacao_arquivos/pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(",")))


if arquivo.close:
    print('Arquivo já foi fechado')
