#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Utilizando decorator'''


def log(function):
    '''Função que vai printar coisas'''
    def decorator(*args, **kwargs):
        '''Função decorator'''
        print(f'Inicio da chamada da função? {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    '''soma'''
    return x + y


@log
def sub(x, y):
    '''subtração'''
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
    print(sub(5, y=7))
