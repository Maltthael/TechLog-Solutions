import sqlite3
from contextlib import contextmanager
class BancoDeDadosLocal(): # cria o banco de dados
    def __init__(self, nome_arquivo='techlog.db'): #nome do banco 
        self.nome_arquivo = nome_arquivo # passa o nome do arquivo
        self.inicializar_banco() # inicia o banco
        


    @contextmanager
    def conectar(self):
        conexao = sqlite3.connect(self.nome_arquivo) #cria conexão com SQLITE
        try:
            yield conexao 
            conexao.commit()
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            conexao.close() # finaliza conexão com o banco quando o adm sair
            
    def inicializar_banco(self):
        with self.conectar() as conexao: # tenta conexão com o banco jogando pra linha 14
            cursor = conexao.cursor() #
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS clientes(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               nome TEXT NOT NULL,
                               email TEXT NOT NULL,
                               telefone TEXT NOT NULL
                           )
                           ''')
            