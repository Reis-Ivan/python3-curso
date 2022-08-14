#!/usr/bin/env python3
'''Callable com (un)packing'''


def calc_preco_final(preco_bruto, calc_imposto, *params):
    '''Função que incide o imposto'''
    return preco_bruto + preco_bruto * calc_imposto(*params)


def imposto_x(importado):
    '''imposto 1'''
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_mult=1):
    '''importo 2'''
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco = 134.98
    preco_final = calc_preco_final(preco, imposto_x, True)
    preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
    print(f'Preço final R$ {preco_final:.2f}')
