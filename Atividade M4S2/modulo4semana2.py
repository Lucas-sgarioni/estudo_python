def decorator_imprimir(func):
    def interna():
        capital = float(input('Digite o capital a ser investido: '))
        taxa = float(input('Digite a taxa a ser utilizada: '))
        tempo = int(input('Digite o tempo (em meses) a ser investido: '))
        resultado = func(capital, taxa, tempo) 
        print(f'CAPITAL: {capital:.2f} TAXA: {taxa} TEMPO: {tempo}')
        print(f'RESULTADO: {resultado:.2f}')
        return resultado
    return interna

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

juros_simples()
