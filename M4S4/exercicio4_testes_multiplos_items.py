import pytest
from exercicio4_adaptado import *

# Referência: https://stackoverflow.com/questions/69364956/assert-in-for-loop-in-python

#Esta função gera dados automaticamente com o formato para o PARAMETRIZE, ou seja, com (entrada desejada, saída correta).
def gerar_pecas_automaticamente(quantidade=1):
    dados = []
    for i in range(quantidade):
        peca = {
            'codigo': i+1,
            'nome': "Nome " + str(i+1),
            'fabricante': "Empresa " + str(i+1),
            'valor': 0.00
        }
        dados.append( (peca, i+1) ) #Salva no formato (Entrada, Saida), que na verdade é (dado simulado, gabarito)
    return dados

#TESTES MÚLTIPLOS COM PARAMETRIZE
dados = gerar_pecas_automaticamente(5)
#Imprime na tela os dados gerados (Rodar pytest com a flag -s)
#Rodar: pytest -s -v .\exercicio4_testes_multiplos_items.py
for dado in dados:
    print(dado)
@pytest.mark.parametrize("peca, codigo", dados)
def test_gerar_codigo_multiplos_dados(peca, codigo):
    assert peca['codigo'] == codigo


#TESTES TRADICIONAIS
def test_gerar_codigo():
    pecas = []
    assert gerar_codigo(pecas) == 1

    pecas = [{'codigo': 1, 'nome': 'Teste', 'fabricante': 'Teste', 'valor': 0.0}, 
             {'codigo': 2, 'nome': 'Teste', 'fabricante': 'Teste', 'valor': 0.0}, 
             {'codigo': 17, 'nome': 'Teste', 'fabricante': 'Teste', 'valor': 0.0}]
    assert gerar_codigo(pecas) == 18
    
# pytest.exe -s -vv -cov=./exercicio4_testes_multiplos_items.py