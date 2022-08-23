#!/usr/bin/env python3.10
'''Desafio de imutabilidade'''
from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce

# Português PT-BR
setlocale(LC_ALL, 'pt_BR.UTF-8')

# Listar todos os meses do ano com 31 dias
# 1. (filter) Pegar os índices de todos os meses com 31 dias
# 2. (map) transformar os índices em nome
# 3. (reduce) juntar tudo par imprmir

meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nome = map(lambda mes: month_name[mes], meses_31)
juntar_meses = reduce(
    lambda todos, nome_mes: f'{todos}\n-{nome_mes}', meses_nome, 'Meses com 31 dias:')

print(juntar_meses)
