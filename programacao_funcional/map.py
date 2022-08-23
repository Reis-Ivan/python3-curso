#!/usr/bin/env python3.10
'''Função MAP'''

lista_1 = [i for i in range(1, 6)]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Carlos', 'idade': 31},
    {'nome': 'Renata', 'idade': 37},
    {'nome': 'Michel', 'idade': 30}
]

so_nomes = map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista_2)
print(sum(so_idades))

# Desafio: usando map() retorne frases '<nome> tem <idade> anos'.

frases = map(lambda di: f"{di['nome']} tem {di['idade']} anos", lista_2)
print(list(frases))
