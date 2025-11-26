from contextlib import asynccontextmanager
from fastapi import FastAPI
from util.database import init_db
from app.models.user import Pessoa, Endereco
from app.controllers.pessoa_controller import router as pessoa_router
from app.controllers.endereco_controller import router as endereco_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação.
    
    Startup: Inicializa o banco de dados
    Shutdown: Limpeza de recursos (se necessário no futuro)
    """
    # Startup
    init_db()
    yield
    # Shutdown (adicione lógica de limpeza aqui se necessário)


app = FastAPI(
    title="API de Cadastro de Pessoas",
    version="1.0.0",
    description="API para gerenciar cadastro de pessoas e seus endereços",
    lifespan=lifespan
)

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

