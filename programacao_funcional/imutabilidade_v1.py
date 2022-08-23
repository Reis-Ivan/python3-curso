#!/usr/bin/env python3.10
from cProfile import label
from locale import setlocale, LC_ALL
from calendar import month_name, mdays
from functools import reduce

# Português PT-BR
setlocale(LC_ALL, 'pt_BR.UTF-8')

# Listar todos os meses do ano com 31 dias

# dic_ano = [{'nome': month_name[i], 'dias': mdays[i]} for i in range(1, 13)]

# mes_31 = list(filter(lambda d: d['dias'] == 31, dic_ano))
# mes_31_nome = list(map(lambda d: d['nome'], mes_31))
# print('Meses com 31 dias:')
# for i in range(len(mes_31_nome)):
#     print(f'-{mes_31_nome[i]}')

