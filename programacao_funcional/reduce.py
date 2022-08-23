#!/usr/bin/env python3.10
'''Função REDUCE'''
from functools import reduce

pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Valentina', 'idade': 7},
    {'nome': 'Enzo', 'idade': 9},
    {'nome': 'Lorenzo', 'idade': 33},
]

soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)
