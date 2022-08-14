#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=unspecified-encoding
'''Apresentação de abertura de arquivos leitura sob demanda (streaming)'''
arquivo = open('manipulacao_arquivos/pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(",")))
arquivo.close()

