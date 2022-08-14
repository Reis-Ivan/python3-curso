#!/usr/bin/env python3
'''Parâmetros Nomeados'''


def tag_bloco(texto, classe='success', inline=False):
    '''Gerador de bloco'''
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco(inline=True, texto='inline'))
    print(tag_bloco('falhou', classe='error'))
