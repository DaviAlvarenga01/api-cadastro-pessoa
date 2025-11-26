from fastapi import FastAPI
from util.database import init_db
from app.models.user import Pessoa, Endereco
from app.controllers.pessoa_controller import router as pessoa_router
from app.controllers.endereco_controller import router as endereco_router

app = FastAPI(
    title="API de Cadastro de Pessoas",
    version="1.0.0",
    description="API para gerenciar cadastro de pessoas e seus endereços"
)

@app.on_event("startup")
def on_startup():
    """Inicializa o banco de dados ao iniciar a aplicação"""
    init_db()

app.include_router(pessoa_router)
app.include_router(endereco_router)

@app.get("/")
def root():
    """Rota raiz - Informações da API"""
    return {
        "message": "API de Cadastro de Pessoas",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

