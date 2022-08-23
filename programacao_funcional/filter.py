#!/usr/bin/env python3.10
'''Função FILTER'''

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Valentina', 'idade': 7},
    {'nome': 'Enzo', 'idade': 9},
    {'nome': 'Lorenzo', 'idade': 33},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nome_grande = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(list(nome_grande))
