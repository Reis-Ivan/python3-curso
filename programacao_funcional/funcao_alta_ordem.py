#!/usr/bin/env python3.10
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
'''High Order Function'''

from funcao_primeira_classe import dobro, quadrado


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == '__main__':
    processar('Dobros de 1 a 10', range(1, 11), dobro)
    processar('Quadrado de 1 a 10', range(1, 11), quadrado)
