#!/usr/bin/env python3.10
'''Achar o maior dividor comum de uma lista'''


def mdc(numeros):
    '''MDC'''
    def calc(div):
        return div if sum(map(lambda x: x % div, numeros)) == 0 else calc(div-1)
    return(calc(min(numeros)))


if __name__ == '__main__':
    print(mdc([21, 7]))  # Resposta: 7
    print(mdc([125, 40]))  # Resposta: 5
    print(mdc([9, 564, 66, 3]))  # Resposta: 3
    print(mdc([55, 22]))  # Resposta: 11
    print(mdc([15, 120]))  # Resposta: 15
    print(mdc([7, 9]))  # Resposta: 1
