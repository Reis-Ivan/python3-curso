#!/usr/bin/env python3.10
# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
from datetime import datetime
from loja import Cliente, Vendedor, Compra


def main():
    '''Função principal'''
    cliente = Cliente('Maria Lima', 44)
    vendedor = Vendedor('Pedro Sampaio', 36, 5000)
    compra1 = Compra(vendedor, datetime.now(), 512)
    compra2 = Compra(vendedor, datetime(2018, 1, 29), 256)
    cliente.registrar_compra(compra1)
    cliente.registrar_compra(compra2)

    print(f'Cliente: {cliente}', '(adulto)' if cliente.is_adulto() else '')
    print(f'Vendedor: {vendedor}')

    valor_total = cliente.total_compras()
    quantidade = len(cliente.compras)
    print(f'Total: {valor_total} em {quantidade} compras')
    print(f'Última compra: {cliente.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
