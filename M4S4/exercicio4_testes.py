from exercicio4_adaptado import *

def testes_gerar_codigo():
    #Teste 1: Cria uma lista vazia para testar se ela será inicializada com Código 1
    pecas = []
    assert gerar_codigo(pecas) == 1

    #Teste 2: Cria uma lista com 5 peças para testar se ela será inicializada com Código 6
    pecas = [] 
    for i in range (5):
        peca = {
            'codigo': i+1,
            'nome': "Teste",
            'fabricante': "Teste",
            'valor': 0.00
        }
        pecas.append(peca)
    assert gerar_codigo(pecas) == 6