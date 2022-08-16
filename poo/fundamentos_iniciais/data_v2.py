#!/usr/bin/env python3.10
'''Principios básicos: contrutor __ini__ e cong. para parêmtros opcionais'''


class Data:
    '''Classe data'''

    def __init__(self, dia=1, mes=1, ano=1970):
        '''Método construtor'''
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        '''Método mágico str que converte objeto no formato str'''
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)  # Criação de novo objeto data

print(d1)

d2 = Data(29, mes=5, ano=1995)

print(d2)
