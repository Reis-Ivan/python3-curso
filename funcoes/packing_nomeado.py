#!/usr/bin/env python3
'''**kwargs'''


def resultado_f1(**podium):
    '''Retorna o resultado da F1 pelo dicinário podium'''
    for posicao, piloto in podium.items():
        print(f'{posicao.capitalize()} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. Vettel')
