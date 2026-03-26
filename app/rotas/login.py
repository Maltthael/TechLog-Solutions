from typing import Annotated
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter, Form, Depends
from app.modelos.cliente import Cliente, ClienteCriarAtualizar
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.banco_de_dados.usuario_repositorio import UsuarioRepositorio
from app.dependencias import obter_cliente_repositorio, obter_usuario_repositorio
from fastapi.templating import Jinja2Templates



router = APIRouter(
    prefix="/login",
)


templates = Jinja2Templates(directory="templates/templates")

@router.get("/", response_class = HTMLResponse)
async def pagina_login(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "login.html"
    )
    
@router.post("/")

async def login(
    usuario_repositorio: Annotated[UsuarioRepositorio, Depends(obter_usuario_repositorio)],
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
):
    usuario = await usuario_repositorio.buscar_usuarios_por_email_senha(email, senha)
    if usuario:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="session_token", value="token-senha", httponly=True)
        return response
    
    
    
    return templates.TemplateResponse(
        request=request,
        name="login.html", # Certifique-se de que o nome do arquivo está aqui
        context={
            "email": email,
            "senha": senha,
            "error": "Credenciais invalidas"
        }
    )
    # Caso contrário, informe que houve uma credencial inválida
    
