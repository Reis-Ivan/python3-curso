#!/usr/bin/env python3.10
'''Generator #1'''


def cores_arco_iris():
    ''' Retorma as cores'''
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))

    while True:
        print(next(generator))
