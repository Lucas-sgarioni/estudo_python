def decorator_valores(func):
    def interna(valor_unitario, quantidade, desconto):
        try:
            valor_unitario = float(valor_unitario)
            quantidade = int(quantidade)
            
            if quantidade > 0 and quantidade < 10:
                desconto = 1
            elif quantidade >= 10 and quantidade <= 99:
                desconto = 0.95
            elif quantidade >= 100 and quantidade <=999:
                desconto = 0.90
            elif quantidade >= 1000:
                desconto = 0.85
            
            valor_com_desconto, valor_sem_desconto, desconto = func(valor_unitario, quantidade, desconto)

            global resultado
            resultado = f'Valor total sem desconto: R$ {valor_sem_desconto:.2f}. Valor total com desconto: R$ {valor_com_desconto:.2f}'
            print(resultado)
            return resultado
        except ValueError:
            erro = 'Você digitou um valor errado.'
            print(erro)
            return erro

    return interna
    
@decorator_valores
def calcula_desconto(valor_unitario, quantidade, desconto):
  
    #No desconto o completo de até 1 é o valor do desconto.
    #ex: 0,85 tem 15% de desconto. -> 1 - 0,85 = 0.15
    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    return valor_com_desconto, valor_sem_desconto, desconto

if __name__ == "__main__":
    valor_unitario = input("Valor unitário do produto: ")
    quantidade = input("Quantidade: ")
    desconto = None
    calcula_desconto(valor_unitario, quantidade, desconto)
    #print(resultado)
