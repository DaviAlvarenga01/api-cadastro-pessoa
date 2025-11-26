from fastapi import FastAPI, HTTPException
from util.database import init_db
from app.models.user import Pessoa, Endereco

app = FastAPI(title="API de Cadastro de Pessoas", version="1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/pessoas")
def criar_pessoa(pessoa: PessoaCreate, session: SessionDep):
    db_pessoa = Pessoa(**pessoa.dict())
    session.add(db_pessoa)
    session.commit()
    session.refresh(db_pessoa)
    return db_pessoa

