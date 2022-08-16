#!/usr/bin/env python3.10
'''Adiciona vencimento ao projeto'''
from datetime import datetime, timedelta


class Projeto:
    '''Gerencia tarefas'''

    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        '''Adiciona uma tarefa a lista de tarefas'''
        self.tarefas.append(Tarefa(descricao, vencimento))

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

    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        '''Método que conclui'''
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        return f'{self.descricao} ' + ' '.join(status)


def main():
    '''Função principal'''
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa', datetime.now())
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa:  # método iter
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no Mercado')
    mercado.add('Frutas Secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, seconds=1))
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:  # método iter
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
