from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.rotas import cliente, login


templates = Jinja2Templates(directory="templates/templates")

app = FastAPI(
    title= "Techlog Solutions API",
    description = "CRM para Techlog Solutions",
    version = "1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name = "static")
app.include_router(cliente.router)
app.include_router(cliente.front_router)
app.include_router(login.router)

@app.get("/health")
async def health_check():
    return {"status": "OK"}

@app.get("/", response_class=HTMLResponse)
async def front_page(request: Request):
     return templates.TemplateResponse(
    request = request, 
    name = "index.html", 
    context = {"titulo": "Techlog Solutions CRM", "versao": "1.0.0"}
)