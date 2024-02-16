import sqlite3
import os

conn = sqlite3.connect('atividade1.sqlite3')
cursor = conn.cursor()

criando_tabela = """
    CREATE TABLE IF NOT EXISTS tarefa(
    id_tarefa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(60) NOT NULL,
    data VARCHAR(10) NOT NULL,
    categoria VARCHAR(30),
    status VARCHAR(3) NOT NULL
    )
"""
cursor.execute(criando_tabela)
conn.commit()

while True:
    
    retorno = input("1 - Incluir tarefa\n2 - Atualizar dados\n3 - Excluir tarefa\n4 - Listar dados\n5 - Listar por data\n6 - Sair\nSelecione a opção que deseja: ")
    if retorno == "1":
        os.system('clear')
        nome = input('Digite o nome da tarefa: ')
        data = input('Digite a data a ser realizada a tarefa: ')
        categoria = input('Digite a categoria da tarefa: ')
        status = input('Digite sim se a tarefa foi realizada e não caso a tarefa ainda não tenha sido realizada: ')
        cursor.execute("INSERT INTO tarefa (nome, data, categoria, status) VALUES (?, ?, ?, ?)", [nome, data, categoria, status])
        conn.commit()
        

    elif retorno == "2":
        selecionar_id = input("Digite o ID da tarefa a ser atualizada: ")
        atualizar_status = input("Digite o novo STATUS da tarefa: ")
        cursor.execute(
        """
        UPDATE tarefa SET (status) = ? WHERE id_tarefa = ?
    """, [atualizar_status, selecionar_id]
    )
        conn.commit()
        os.system('clear')
    elif retorno == "3":
        selecionar_id = input("Digite o ID da tarefa a ser EXCLUÍDA: ")
        cursor.execute("""DELETE FROM tarefa WHERE id_tarefa = ?""" , [selecionar_id])
        conn.commit()
        os.system('clear')

    #código para listar
    elif retorno == "4":
        os.system('clear')
        cursor.execute(""" SELECT * FROM tarefa""")
        resultados = cursor.fetchall()
        print("------- Lista de Tarefas-------")
        for resultado in resultados:   
            print(resultado)

    #código para listar conforme data
    elif retorno == "5":
        data_selecionada = input("Selecione a data das tarefas a serem listadas: ")
        cursor.execute("""
            SELECT *
            FROM tarefa
            WHERE data = ?
            """, [data_selecionada]
        )

        resultados = cursor.fetchall()
        
        print("------- Lista de Tarefas-------")
        for resultado in resultados:   
            print(resultado)

    elif retorno == "6":
        break
        
    else:
        print("Você digitou uma opção INVÁLIDA!")
conn.commit()
conn.close()