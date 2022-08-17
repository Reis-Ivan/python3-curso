#!/usr/bin/env python3.10
# pylint: disable=unused-argument
'''Métodos privados'''
from datetime import datetime, timedelta


class Projeto:
    '''Gerencia tarefas'''

    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def _add_tarefa(self, tarefa, **kwargs):
        '''Método "privado""'''
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        '''Adiciona uma tarefa a lista de tarefas'''
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

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


class TarefaRecorrente(Tarefa):
    '''Classe filha que herda do pai'''

    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    '''Função principal'''
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar Roupa', datetime.now())
    casa.add('Lavar Prato')
    casa.add(TarefaRecorrente('Trocar Lençóis', datetime.now(), 7))
    casa.add(casa.procurar('Trocar Lençóis').concluir())
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
