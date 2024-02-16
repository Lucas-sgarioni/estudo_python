import pytest

from exercicio1 import calcula_desconto

def test_calcula_desconto():
    assert calcula_desconto(500, 1, None) == 'Valor total sem desconto: R$ 500.00. Valor total com desconto: R$ 500.00'
    assert calcula_desconto(500, 10, None) == 'Valor total sem desconto: R$ 5000.00. Valor total com desconto: R$ 4750.00'
    assert calcula_desconto(500, 50, None) == 'Valor total sem desconto: R$ 25000.00. Valor total com desconto: R$ 23750.00'
    assert calcula_desconto(50, 500, None) == 'Valor total sem desconto: R$ 25000.00. Valor total com desconto: R$ 22500.00'
    assert calcula_desconto(5, 5000, None) == 'Valor total sem desconto: R$ 25000.00. Valor total com desconto: R$ 21250.00'
    assert calcula_desconto('a', 50, None) == 'Você digitou um valor errado.'
    assert calcula_desconto(50, 'a', None) == 'Você digitou um valor errado.'
