import sqlite3
import os

conexao = sqlite3.connect('atividade2.sqlite3')
cursor = conexao.cursor()
#criação das tabelas
tabela_evento = """
    CREATE TABLE IF NOT EXISTS evento(
    titulo VARCHAR(60) NOT NULL,
    data VARCHAR(10) NOT NULL,
    local VARCHAR(60),
    organizador_cpf VARCHAR(11) NOT NULL,
    FOREIGN KEY (organizador_cpf) REFERENCES organizador (cpf)
    )
"""

tabela_organizador = """
    CREATE TABLE IF NOT EXISTS organizador(
    nome VARCHAR(60) NOT NULL,
    email VARCHAR(60) NOT NULL,
    cpf VARCHAR(11) NOT NULL PRIMARY KEY
    )
"""

cursor.execute(tabela_evento)
cursor.execute(tabela_organizador)
conexao.commit()

#função para cadastrar eventos
def incluir_evento():
    os.system('clear')
    titulo = input('Digite o título do evento: ').title()
    data = input('Digite a data de realização do evento: ')
    local = input('Digite o local a ser realizado o evento: ').lower()
    organizador_cpf = input('Digite o CPF do organizador: ')
    cursor.execute("INSERT INTO evento (titulo, data, local, organizador_cpf) VALUES (?, ?, ?, ?)", (titulo, data, local, organizador_cpf))
    conexao.commit()

#código para cadastrar novos organizadores
def incluir_organizador():
    os.system('clear')
    nome = input('Digite o nome do organizador: ').title()
    cpf = input('Digite o CPF do organizador: ')
    email = input('Digite o e-mail de contato do organizador: ').lower()
    cursor.execute("INSERT INTO organizador (nome, cpf, email) VALUES (?, ?, ?)", (nome, cpf, email))
    conexao.commit()

while True:
    retorno = input("1 - Incluir evento\n2 - Incluir organizador\n3 - Listar eventos\n4 - Listar organizadores\n5 - Sair\nSelecione a opção que deseja: ")
    if retorno == "1":
        retorno = input('O organizador do evento já possui cadastro? (S)im ou (N)ão: ').title()
        if retorno == 'S':
            incluir_evento()
        elif retorno == 'N':
            incluir_organizador()
            incluir_evento()
        else:
            print('Você digitou uma opção inválida!')

    elif retorno == "2":
        incluir_organizador()

    #código para listar eventos
    elif retorno == "3":
        os.system('clear')
        cursor.execute(""" SELECT evento.titulo, evento.data, evento.local, organizador.nome FROM evento JOIN organizador ON cpf = organizador_cpf""")
        resultados = cursor.fetchall()
        print("------- Lista de Eventos-------")
        print(f'Título {resultados[0][0]}')
        print(f'Data {resultados[0][1]}')
        print(f'Local {resultados[0][2]}')
        print(f'Organizador {resultados[0][3]}')

    #código para listar organizadores
    elif retorno == "4":
        os.system('clear')
        cursor.execute(""" SELECT organizador.nome, organizador.cpf, organizador.email FROM organizador""")
        resultados = cursor.fetchall()
        print("------- Lista de Tarefas-------")
        print(f'Nome: {resultados[0][0]}')
        print(f'CPF: {resultados[0][1]}')
        print(f'E-mail: {resultados[0][2]}')

    #código para sair do while
    elif retorno == "5":
        break
    
    #código caso o retorno seja diferente das opções disponíveis
    else:
        print("Você digitou uma opção INVÁLIDA!")

conexao.commit()
conexao.close()
