#!/usr/bin/env python3.10
'''Funções LAMBDA'''
compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

totais = tuple(
    map(
        lambda cpr: cpr['quantidade'] * cpr['preco'], compras
    )
)

print('Preços totais:', list(totais))
print('Total geral:', sum(totais))
