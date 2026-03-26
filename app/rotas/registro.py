from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.banco_de_dados.usuario_repositorio import UsuarioRepositorio, UsuarioCriarAtualizar
from app.dependencias import obter_usuario_repositorio

router = APIRouter(
    prefix="/registro"
)

templates = Jinja2Templates(directory="templates/templates")

@router.get("/", response_class=HTMLResponse)
async def pagina_registro(request: Request):
    return templates.TemplateResponse(
        request = request,
        name ="registro.html", 
        )



@router.post("/")
async def registrar_usuario(
    usuario_repositorio: Annotated[UsuarioRepositorio, Depends(obter_usuario_repositorio)],
    request: Request,
    nome = Form(...),
    email = Form(...),
    senha = Form(...),
    confirma_senha: str = Form(...),
):
    
    if senha != confirma_senha:
        data = {
            "nome": nome,
            "email": email,
            "senha": senha,
            "confirma_senha": confirma_senha,
        }

    if not all([email, senha, nome, confirma_senha]):
            return templates.TemplateResponse(
                name = "registro.html", 
                request = request,
                context = {"Campos obrigatórios faltantes"},
                **data
            )
    
    
    usuario_criar = UsuarioCriarAtualizar(nome=nome, email=email, senha=senha)
    usuario = await usuario_repositorio.criar_usuario(usuario_criar)
   
    
    if usuario:
        response = RedirectResponse(url="/login", status_code=303)
        return response 