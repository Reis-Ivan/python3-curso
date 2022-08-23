#!/usr/bin/env python3.10
# pylint: disable=missing-function-docstring
'''Aula 1 POO Avançada'''


class Humano:
    ''' classe humano'''
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('Jose')
    # sempre que um método retorna self pode-se chamar outros metodos encadeados
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')
