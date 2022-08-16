#!/usr/bin/env python3.10
'''Desafio classe Carro'''


class Carro:
    '''Classe Carro'''

    def __init__(self, vel_max, vel_atual=0):
        self.vel_max = vel_max
        self.vel_atual = vel_atual

    def acelerar(self, delta=5):
        '''Método que retorna a velocidade acelerada'''

        if self.vel_atual < self.vel_max:
            self.vel_atual += delta
        else:
            self.vel_atual = self.vel_max
        return self.vel_atual

    def frear(self, delta=5):
        '''Método que retorna a velocidade freada'''
        if self.vel_atual > 0:
            self.vel_atual -= delta
        else:
            self.vel_atual = 0
        return self.vel_atual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
