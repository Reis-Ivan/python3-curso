#!/usr/bin/env python3.10
# pylint: disable=attribute-defined-outside-init
'''Principios básicos: criação de classe e método mágico __str__'''


class Data:
    '''Classe data'''

    def __str__(self):
        '''Método mágico str que converte objeto no formato str'''
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()  # Criação de novo objeto data
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 29
d2.mes = 1
d2.ano = 1995
print(d2)
