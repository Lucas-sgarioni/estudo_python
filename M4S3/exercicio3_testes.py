from exercicio3_adaptado import *

#INCOMPLETO, PODEMOS MELHORAR

def testes_calcular_multiplicador_rota():
    assert calcular_multiplicador_rota('rs') == 1.0
    assert calcular_multiplicador_rota('sr') == 1.0
    assert calcular_multiplicador_rota('bs') == 1.2
    assert calcular_multiplicador_rota('sb') == 1.2
    assert calcular_multiplicador_rota('br') == 1.5
    assert calcular_multiplicador_rota('rb') == 1.5
    assert calcular_multiplicador_rota('xx') == "Indefinido"