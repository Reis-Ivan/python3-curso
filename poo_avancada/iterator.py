#!/usr/bin/env python3.10
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
'''Aula sobre iterator'''


class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError as err:
            raise StopIteration() from err


if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))
    try:
        print(next(cores))
    except StopIteration:
        print('Acabou!')

    for cor in RGB():
        print(cor)
