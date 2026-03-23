from fastapi import FastAPI
from fastapi.responses import HTMLResponse 

app = FastAPI(
    title= "Techlog Solutions API",
    description = "CRM para Techlog Solutions",
    version = "1.0.0",
)

@app.get("/")
async def health_check():
    return {"status": "OK"}

@app.get("/front", response_class=HTMLResponse)
@app.get("/front", response_class=HTMLResponse)
async def front_page():
    html_content = """
    <html>
        <head>
            <title>Techlog Solutions</title>
        </head>
        <body>
            <h1>🔪 Techlog Solutions</h1>
            <p>Sistema de Gestão de Ordens de Serviço</p>
            <p>Status: <strong>Operacional</strong></p>
        </body>
    </html>
    """
    return html_content