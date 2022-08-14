#!/usr/bin/env python3
# pylint: disable=consider-using-f-string
'''Introdução ao módulo CSV'''
import csv

with open('manipulacao_arquivos/pessoas.csv', encoding='UTF-8') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))
