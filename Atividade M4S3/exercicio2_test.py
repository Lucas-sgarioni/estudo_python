import pytest

from exercicio2 import *

def test_total_pagar():
    assert total_pagar(4) == 'O total a ser pago é R$ 4.00'
    assert total_pagar(5.231423) == 'O total a ser pago é R$ 5.23'


def test_escolha():
    assert escolha('100') == 'Você pediu um Cachorro Quente no valor de R$ 9.50'
    assert escolha('101') == 'Você pediu um Cachorro Quente Duplo no valor de R$ 11.00'
    assert escolha('102') == 'Você pediu um X-Egg no valor de R$ 12.00'
    assert escolha('103') == 'Você pediu um X-Salada no valor de R$ 12.95'
    assert escolha('104') == 'Você pediu um X-Bacon no valor de R$ 14.50'
    assert escolha('105') == 'Você pediu um X-Tudo no valor de R$ 17.00'
    assert escolha('200') == 'Você pediu um Refrigerante Lata no valor de R$ 5.50'
    assert escolha('201') == 'Você pediu um Chá Gelado no valor de R$ 4.95'
    assert escolha('10') == 'Opção inválida'