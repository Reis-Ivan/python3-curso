#!/usr/bin/env python3.10
'''Funções Imutabilidade #2 - Trabalhar com dados imutáveis (tuplas, strings...)'''
from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94)

print(sorted(valores))
print(valores)

# valores.sort()
# print(valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(tuple(reversed(valores)))
print(valores)
# valores.reverse()
# print(valores)
