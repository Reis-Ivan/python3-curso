#!/usr/bin/env python3.10
# pylint: disable=expression-not-assigned
'''Projeto lista de tarefas'''
from datetime import datetime


class Tarefa:
    '''Gerencia tarefas'''

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
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa:
        print(f'- {tarefa}')


main()
