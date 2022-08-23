#!/usr/bin/env python3.10
# pylint: disable=C0116
# Implementação simplificada do map

def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    print(tuple(mapear(lambda x: x ** 2, [2, 3, 4])))
