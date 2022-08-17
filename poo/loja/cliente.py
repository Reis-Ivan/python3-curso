# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
from .pessoa import Pessoa


def get_data(compra):
    '''Pega a data da compra'''
    return compra.data


class Cliente(Pessoa):
    '''Classe cliente que herda de pessoa'''

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.compras = []

    def registrar_compra(self, compra):
        '''Registra uma compra na lista de compras'''
        self.compras.append(compra)

    def get_data_ultima_compra(self):
        '''Retorna a data da última compra'''
        return None if not self.compras else \
            sorted(self.compras, key=get_data)[-1].data

    def total_compras(self):
        '''Retorn o total das compras'''
        total = 0
        for compra in self.compras:
            total += compra.valor
        return total
