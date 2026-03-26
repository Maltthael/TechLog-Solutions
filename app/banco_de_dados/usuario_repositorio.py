from app.banco_de_dados.local import BancoDeDadosLocal
from app.modelos.usuario import Usuario

class UsuarioRepositorio:
    def __init__(self, banco_de_dados: BancoDeDadosLocal):
        self.bd = banco_de_dados
        
    async def buscar_usuarios_por_email_senha(self) -> Usuario | None:
            with self.bd.conectar() as conexao:
                cursor = conexao.cursor()
                cursor.execute("SELECT id, nome, email,  FROM usuarios WHERE email = ?")
                linha = cursor.fetchone()
                if linha:
                    return Usuario(id_ = linha[0], nome = linha[1], email = linha[2])
                return None
  