import requests

class TabelaFipe:
    def __init__(self):
        url_marcas = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
        headers = { "User-Agent": "Test" } 
        response = requests.get(url_marcas, headers= headers)

        if response.status_code == 200:
            marcas = response.json()
            for marca in marcas:
                print(f"Marca: {marca['nome']}, Código: {marca['codigo']}")
        else:
            print("Erro ao fazer a chamada: ", response.status_code)
        print()
        
    def get_modelo(id_value):

        url_carros = "https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos"
        url_carros = url_carros.format(id_value)
        response = requests.get(url_carros) 
        if response.status_code == 200:
            carros = response.json()['modelos']
            for carro in carros:
               print(f"Carro: {carro['nome']}")        
        else:
            print("Erro ao fazer a chamada: ", response.status_code)
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current < len(self.response):
            raise StopIteration
        
        result = self.modelos[self.current]
        self.current += 1
        return result

while True:
    retorno = input("1 - Listar marcas\n2 - Sair\nEscolha uma opção: ")
    if retorno == "1":
        user = TabelaFipe()
        retono_marca = input("Digite o código da marca desejada: ")
        user = TabelaFipe.get_modelo(id_value=retono_marca)
    elif retorno == "2":
        break
    else:
        print("Opção inválida!")