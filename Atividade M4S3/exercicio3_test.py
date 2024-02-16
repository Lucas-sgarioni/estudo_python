import pytest

from exercicio3 import *

def test_validar_medida():
    assert validar_medida('4') == 4
    assert validar_medida('6') == 6
    assert validar_medida('5.94') == -1
    assert validar_medida('a') == -1

def test_calcular_preco_volume():
    assert calcular_preco_volume(500) == 10.0
    assert calcular_preco_volume(1000) == 20.0
    assert calcular_preco_volume(20000) == 30.0
    assert calcular_preco_volume(50000) == 40.0

def test_calcular_multiplicador_peso():
    assert calcular_multiplicador_peso(0.0) == 1.0
    assert calcular_multiplicador_peso(0.5) == 1.5
    assert calcular_multiplicador_peso(5.0) == 2.0
    assert calcular_multiplicador_peso(15.5) == 3.0

def test_calcular_multiplicador_rota():
    assert calcular_multiplicador_rota('rs') == 1.0
    assert calcular_multiplicador_rota('sr') == 1.0
    assert calcular_multiplicador_rota('bs') == 1.2
    assert calcular_multiplicador_rota('sb') == 1.2
    assert calcular_multiplicador_rota('br') == 1.5
    assert calcular_multiplicador_rota('rb') == 1.5

def test_calcular_frete():
    assert calcular_frete(20, 3.0, 1.2) == 72.00
    assert calcular_frete(20, 1.0, 1.5) == 30.00
