#!/usr/bin/env python3
# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
'''Desafio do tópico de funções'''


def tag(tag, *args, **kwargs):
    '''Função do problem'''
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    atts = ' '.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {atts}>{inner}</{tag}'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )
