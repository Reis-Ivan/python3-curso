#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=unspecified-encoding
'''O bloco de finally sempre é executado'''
try:
    arquivo = open('manipulacao_arquivos/pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(",")))
finally:
    print('finally')
    arquivo.close()

if arquivo.close:
    print('Arquivo já foi fechado')
