from exercicio4 import *

def test_gerar_codigo():
    pecas = []
    assert gerar_codigo(pecas) == 1

    pecas = []
    for i in range(5):
        peca = {
            'codigo': i+1,
            'nome': "Teste",
            'fabricante': "Teste",
            'valor': 0.00
        }
        pecas.append(peca)
    assert gerar_codigo(pecas) == 6