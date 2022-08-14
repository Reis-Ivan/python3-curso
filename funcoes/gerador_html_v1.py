'''Parametros opcionais'''


def tag_bloco(texto, classe='success'):  # Valor padrão para classe
    '''Gerador de bloco'''
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="success">Incluido com sucesso!</div>'

    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'

    print(tag_bloco('bloco'))
