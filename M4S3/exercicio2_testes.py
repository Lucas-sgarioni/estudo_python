from exercicio2_adaptado import *

def testes_realizar_pedido():
    #Teste 1: Testar pedidos individualmente
    assert realizar_pedido(100) == 9.00
    assert realizar_pedido(101) == 11.00
    assert realizar_pedido(102) == 12.00
    assert realizar_pedido(103) == 12.00
    assert realizar_pedido(104) == 14.00
    assert realizar_pedido(105) == 17.00
    assert realizar_pedido(200) == 5.00
    assert realizar_pedido(201) == 4.00
    assert realizar_pedido(300) == None #Checa códigos inexistentes
    assert realizar_pedido(400) == None #Checa códigos inexistentes