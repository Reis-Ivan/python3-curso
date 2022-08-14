'''Resolução do desafio'''

import csv

with open('manipulacao_arquivos/desafio-ibge.csv', encoding='ISO-8859-1') as entrada:
    for dados in csv.reader(entrada):
        print(f'{dados[8]}: {dados[3]}')

if entrada.close:
    print('Entrada foi fechada')
