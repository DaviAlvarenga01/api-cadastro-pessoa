from fastapi import APIRouter, status
from typing import List
from util.database import SessionDep
from app.schemas.dto import PessoaCreate, PessoaRead, PessoaUpdate, EnderecoRead
from app.services.pessoa_service import PessoaService
from app.services.endereco_service import EnderecoService

router = APIRouter(prefix="/pessoas", tags=["Pessoas"])


@router.post("", response_model=PessoaRead, status_code=status.HTTP_201_CREATED)
def criar_pessoa(pessoa: PessoaCreate, session: SessionDep):
    """
    Cria uma nova pessoa.
    
    - **nome**: Nome completo da pessoa
    - **idade**: Idade (opcional)
    - **email**: Email único
    """
    return PessoaService.criar_pessoa(pessoa, session)


@router.get("", response_model=List[PessoaRead])
def listar_pessoas(session: SessionDep):
    """Lista todas as pessoas cadastradas com seus endereços."""
    return PessoaService.listar_pessoas(session)


@router.get("/{pessoa_id}", response_model=PessoaRead)
def buscar_pessoa(pessoa_id: int, session: SessionDep):
    """Busca uma pessoa específica por ID."""
    return PessoaService.buscar_pessoa(pessoa_id, session)


@router.put("/{pessoa_id}", response_model=PessoaRead)
def atualizar_pessoa(pessoa_id: int, pessoa: PessoaUpdate, session: SessionDep):
    """
    Atualiza os dados de uma pessoa.
    
    Todos os campos são opcionais - apenas os fornecidos serão atualizados.
    """
    return PessoaService.atualizar_pessoa(pessoa_id, pessoa, session)


@router.delete("/{pessoa_id}", status_code=status.HTTP_200_OK)
def deletar_pessoa(pessoa_id: int, session: SessionDep):
    """
    Deleta uma pessoa e todos os seus endereços (cascade).
    
    ⚠️ Ação irreversível!
    """
    return PessoaService.deletar_pessoa(pessoa_id, session)


@router.get("/{pessoa_id}/enderecos", response_model=List[EnderecoRead])
def listar_enderecos_pessoa(pessoa_id: int, session: SessionDep):
    """Lista todos os endereços de uma pessoa específica."""
    return EnderecoService.listar_enderecos_pessoa(pessoa_id, session)
