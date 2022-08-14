#!/usr/bin/env python3
'''Introdução packing e unpacking'''


def soma_2(a, b):
    '''Função de exemplo'''
    return a + b


def soma_3(a, b, c):
    '''Função de exemplo'''
    return a+b+c


def soma_n(*numeros):
    '''* indica uma tupla'''
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))

    # packing
    print(soma_n(1))
    print(soma_n(1, 2, 3))
    print(soma_n(1, 2, 3, 4, 5, 6, 7))

    # unpacking
    tupla_nums = (1, 2, 3)
    print(soma_n(*tupla_nums))
    lista_nums = [1, 2, 3]
    print(soma_n(*lista_nums))
