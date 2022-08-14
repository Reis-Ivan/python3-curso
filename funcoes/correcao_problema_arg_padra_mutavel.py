#!/usr/bin/env python3
'''Resolução do problema com argumento mutável'''


def fibonacci(sequencia=None):
    '''Uso de mutáveis como valor default (armadilha)'''
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
