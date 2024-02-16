from exercicio1_adaptado import *

def testes_calcula_desconto():
    assert calcula_desconto(4) == 1.00
    assert calcula_desconto(25) == 0.95
    assert calcula_desconto(549) == 0.90
    assert calcula_desconto(1600) == 0.85
    assert calcula_desconto(-5) == None
    assert calcula_desconto("lalala") == "Erro 101"
    assert calcula_desconto(True) == "Erro 102"