#!/usr/bin/env python3.10
'''Desafio de imutabilidade'''
from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce

# Português PT-BR
setlocale(LC_ALL, 'pt_BR.UTF-8')


def mes_com_31(mes):
    '''Retorna os indices'''
    return mdays[mes] == 31


def get_nome_mes(mes):
    '''Retorns os nomes'''
    return month_name[mes]


def juntar_meses(todos, nome_mes):
    '''Exibe a lista'''
    return f'{todos}\n- {nome_mes}'


print(reduce(juntar_meses, map(get_nome_mes, filter(
    mes_com_31, range(1, 13))), 'Meses com 31 dias:'))
