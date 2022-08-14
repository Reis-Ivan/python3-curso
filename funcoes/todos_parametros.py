#!/usr/bin/env python3
'''Acessando todos os parâmetros'''


def todos_params(*args, **kwargs):
    '''Imprime todos os parâmetros'''
    print(f'args: {args}')
    print(f'kargs: {kwargs}')


if __name__ == '__main__':
    # args =>posicionais - tupla
    # kwargs => nomeado - dicinário

    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    todos_params(primeiro='João', segundo='Maria')
    todos_params('Maria', primeiro='João')
