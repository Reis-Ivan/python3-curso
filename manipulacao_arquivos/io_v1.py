#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=consider-using-f-string
# pylint: disable=unspecified-encoding
'''Apresentação de abertura de arquivos'''
arquivo = open('manipulacao_arquivos/pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():  # splitline vai quebrar o arquivo em linhas
    print("Nome: {}, Idade: {}".format(*registro.split(",")))
