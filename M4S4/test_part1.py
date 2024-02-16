import pytest

def multiplicacao(x, y):
    return x*y

def teste_multiplicacao1():
    assert multiplicacao(10, 2) == 20

def teste_multiplicacao2():
    assert multiplicacao(9, 3) == 27

def teste_multiplicacao3():
    assert multiplicacao(10, 9) == 90

def teste_quadrado1():
    assert multiplicacao(4, 4) == 16

def teste_quadrado2():
    assert multiplicacao(6, 6) == 36