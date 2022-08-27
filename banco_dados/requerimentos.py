#!/usr/bin/env python3.10
'''Requerimento'''
try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL Connector não instalado!')
else:
    print('MySQL Connector instalado e pronto!')
