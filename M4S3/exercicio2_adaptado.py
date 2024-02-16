def menu():
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerente Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)


def realizar_pedido(codigo):
    valor = None
    
    if codigo == 100:
        print('Você pediu um Cachorro Quente no valor de 9,00')
        valor = 9.00
    elif codigo == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        valor = 11.00
    elif codigo == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        valor = 12.00
    elif codigo == 103:
        print('Você pediu um X-Salada no valor de 12,00')
        valor = 12.00
    elif codigo == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        valor = 14.00
    elif codigo == 105:
        print('Você pediu um X-Tudo no valor de 17,00')
        valor = 17.00
    elif codigo == 200:
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        valor = 5.00
    elif codigo == 201:
        print('Você pediu um Chá Gelado no valor de 4,00')
        valor = 4.00
    else:
        print('Opção inválida')
    return valor #Retorna o valor a partir do código

if __name__ == '__main__':
    menu() #Apresenta o menu na tela

    total = 0.0

    while True:
        codigo = int(input('Entre com o código desejado: '))
        total += realizar_pedido(codigo) #Passa o código por parametro para a função e obtém o valor do produto desejado
        
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = int(input("Digite a opção desejada: "))

        if pedir_mais == 2:
            break

    print(f'O total a ser pago é: {total:.2f} R$')
