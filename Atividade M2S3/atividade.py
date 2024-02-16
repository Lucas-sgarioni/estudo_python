import sqlite3

conn = sqlite3.connect('atividade.sqlite3')
cursor = conn.cursor()

criando_tabela = """
    CREATE TABLE IF NOT EXISTS fornecedor(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    produto TEXT NOT NULL
    )
"""
cursor.execute(criando_tabela)
conn.commit()
'''
inserindo_valores = """
    INSERT INTO fornecedor (id, nome, endereco, produto) VALUES
    (1, 'Empresa de Leite Parmaleite', 'Rua dos Leites, 23', 'Leite'),
    (2, 'Peixaria Abril', 'Rua dos Leites, 26', 'Peixe'),
    (3, 'Açougue Legal', 'Rua das Carnes, 30', 'Carnes'),
    (4, 'Açougue Novo', 'Rua das Carnes, 50', 'Carnes')
"""

cursor.execute(inserindo_valores)
conn.commit()
'''
'''
#foi solicitado na tarefa para utilizar o comando INSERT e não UPDATE, sendo assim
#os valores 3 e 4 solicitados na atividade já estão em uso e passei para id 5 e 6
novos_valores = """
    INSERT INTO fornecedor (id, nome, endereco, produto) VALUES
    (5, 'Padaria do Pão', 'Rua das Baguetes, 54', 'Pão'),
    (6, 'Marcenaria Martelo', 'Rua dos Móveis, 34', 'Móveis')
"""
cursor.execute(novos_valores)
conn.commit()
'''
atualizar = """
    UPDATE fornecedor SET endereco = 'Rua dos Peixes, 26' WHERE id = 2
"""
cursor.execute(atualizar)
conn.commit()

selecionar = """
    SELECT id, nome, endereco, produto FROM fornecedor
"""
cursor.execute(selecionar)
conn.commit()

selecionar_carne = """
    SELECT id, nome, endereco, produto FROM fornecedor WHERE produto = 'Carnes'
"""
cursor.execute(selecionar_carne)
conn.commit()

excluir = """
    DELETE FROM fornecedor WHERE id = 1
"""
conn.execute(excluir)
conn.commit()
conn.close()