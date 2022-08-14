#!/usr/bin/env python3
'''Importação direta de funções dos módulos'''
from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao as sub

print('Soma', soma(3, 2))
print('Subtraçãi', sub(3, 2))
