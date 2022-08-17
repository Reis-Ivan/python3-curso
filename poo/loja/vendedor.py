# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
from .pessoa import Pessoa


class Vendedor(Pessoa):
    '''Classe Vendedor do tipo Pessoa'''

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
