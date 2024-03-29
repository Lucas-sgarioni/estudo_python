def calcula_desconto(quantidade):
    desconto = None
    
    if type(quantidade) == str:
        return "Erro 107" #Tipo de dados inconsistente
    if type(quantidade) == bool:
        return "Erro 102" #Tipo de dados inconsistente

    if quantidade > 0 and quantidade < 10:
        desconto = 1
    elif quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    return desconto

if __name__ == '__main__':
    valor_unitario = float(input('Valor unitário do produto: '))
    quantidade = int(input('Quantidade: '))
    desconto = calcula_desconto(quantidade)

    # No desconto o completo de até 1 é o valor do desconto.
    # Ex: 0,85 tem 15% de desconto. -> 1 - 0,85 = 0.15

    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    print(f'Valor total sem desconto: {valor_sem_desconto:.2f} R$')
    print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')
