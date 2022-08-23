#!/usr/bin/env python3.10
'''Listar todos os meses do ano com 31 dias'''
from locale import setlocale, LC_ALL
from calendar import month_name, mdays

# Português PT-BR
setlocale(LC_ALL, 'pt_BR.UTF-8')
print('Meses com 31 dias:')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'-{month_name[mes]}')
