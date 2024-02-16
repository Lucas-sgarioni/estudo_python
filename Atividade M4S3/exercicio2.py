
cardapio = [
    {'codigo': '100', 'Descrição': 'Cachorro Quente', 'Valor': 9.50},
    {'codigo': '101', 'Descrição': 'Cachorro Quente Duplo', 'Valor': 11.00},
    {'codigo': '102', 'Descrição': 'X-Egg', 'Valor': 12.00},
    {'codigo': '103', 'Descrição': 'X-Salada', 'Valor': 12.95},
    {'codigo': '104', 'Descrição': 'X-Bacon', 'Valor': 14.50},
    {'codigo': '105', 'Descrição': 'X-Tudo', 'Valor': 17.00},
    {'codigo': '200', 'Descrição': 'Refrigerante Lata', 'Valor': 5.50},
    {'codigo': '201', 'Descrição': 'Chá Gelado', 'Valor': 4.95},
    ]

total = 0.0

def total_pagar(total):
    return f'O total a ser pago é R$ {total:.2f}'

def escolha(codigo):
    global total
    for item in cardapio:
        if item['codigo'] == codigo:
            resultado = f'Você pediu um {item["Descrição"]} no valor de R$ {item["Valor"]:.2f}'
            total += item['Valor']
            print(total_pagar(total))           
            return resultado
    else:
        returno = 'Opção inválida' 
        return returno
 
if __name__ == '__main__':
    visual = """
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
    print(visual)
    while True:
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = input('Digite uma opção: ')
    
        if pedir_mais == '1':
            print(visual)
            codigo = input('Entre com o código desejado: ')
            print(escolha(codigo))
        elif pedir_mais == '2':
            print(total_pagar(total))
            print('Estamos preparando seu pedido, por favor aguarde.')
            break
        else:
            print('Opção inválida!')