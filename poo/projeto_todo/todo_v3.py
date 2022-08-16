#!/usr/bin/env python3.10
'''Projeto lista de tarefas'''
from datetime import datetime


class Projeto:
    '''Gerencia tarefas'''

    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao):
        '''Adiciona uma tarefa a lista de tarefas'''
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        '''Retorna uma lista de  tarefas pendentes'''
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        '''Possivel IndexError - retonar uma tarefa'''
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas(s) pendentes(s))'


class Tarefa:
    '''Tarefas'''

    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        '''Método que conclui'''
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')


def main():
    '''Função principal'''
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa')
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa:  # método iter
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no Mercado')
    mercado.add('Frutas Secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:  # método iter
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
