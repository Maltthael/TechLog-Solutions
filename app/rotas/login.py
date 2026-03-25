from typing import Annotated
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter, Form
from app.modelos.cliente import Cliente, ClienteCriarAtualizar
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import obter_cliente_repositorio
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
async def login(request: Request, email: str = Form(...), senha: str = Form(...)):
    if email == "admin@techlog.com.br" and senha == "senha123":
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="session_token", value="token-senha", httponly=True)
        return response
    
    
    return templates.TemplateResponse(
        request=request,
        name="login.html", 
        context={          
            "email": email,
            "senha": senha,
            "error": "Credenciais inválidas"
        }
    )
    
