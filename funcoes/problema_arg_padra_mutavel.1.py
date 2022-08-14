#!/usr/bin/env python3
# pylint: disable=invalid-name
'''Exemplo de problema com argumento mutável'''


def fibonacci(sequencia=[0, 1]):
    '''Uso de mutáveis como valor default (armadilha)'''
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()  # cuidado
    print(restart, id(restart))
    assert restart == [0, 1, 1]
