#!/usr/bin/env python3
'''Callable'''


def executar(funcao):
    '''Função com parâmetro que é uma função'''
    if callable(funcao):
        funcao()


def bom_dia():
    '''Ex1'''
    print('Bom dia!')


def bom_tarde():
    '''Ex2'''
    print('Bom tarde!')


if __name__ == '__main__':
    executar(bom_dia)
    executar(bom_tarde)
    executar(1)
