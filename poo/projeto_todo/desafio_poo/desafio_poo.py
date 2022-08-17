#!/usr/bin/env python3.10
'''Desafio Programação Orientada a Objetos'''


class Pessoa:
    '''Classe pessoa'''

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.adulto = True

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

    def is_adulto(self):
        '''Adulto'''
        return self.adulto


class Vendedor(Pessoa):
    '''Vendedor'''

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Cliente(Pessoa):
    '''Classe Pessoa'''

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def regista_compra(self, compra, **kwargs):
        '''Regista na lista de compras uma compra'''
        self.compras.append(Compra(compra, **kwargs))

    def get_data_ultima_compra(self):
        '''Retorna a data da última compra'''
        return self.compras[-1].data

    def total_compras(self):
        '''Retorno o total de compras'''
        total = 0
        total_compras = self.compras
        for i in total_compras:
            total += i.valor
        return total


class Compra():
    '''Classe compra'''

    def __init__(self, vendedor, data, valor):
        self.vendedor = vendedor
        self.data = data
        self.valor = valor
