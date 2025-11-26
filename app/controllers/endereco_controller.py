from fastapi import APIRouter, status
from util.database import SessionDep
from app.schemas.dto import EnderecoCreate, EnderecoRead, EnderecoUpdate
from app.services.endereco_service import endereco_service

router = APIRouter(prefix="/enderecos", tags=["Endereços"])


@router.post("", response_model=EnderecoRead, status_code=status.HTTP_201_CREATED)
def criar_endereco(endereco: EnderecoCreate, session: SessionDep):
    """
    Cria um novo endereço vinculado a uma pessoa.
    
    - **pessoa_id**: ID da pessoa (deve existir)
    - **logradouro**: Rua, avenida, etc. (mínimo 3 caracteres)
    - **numero**: Número do endereço (máximo 10 caracteres)
    - **estado**: UF com 2 letras maiúsculas (ex: SP, RJ)
    - **cidade**: Nome da cidade (mínimo 2 caracteres)
    - **bairro**: Nome do bairro (mínimo 2 caracteres)
    - **cep**: CEP no formato 12345-678 ou 12345678 (opcional)
    """
    return endereco_service.criar(endereco, session)


@router.get("/{endereco_id}", response_model=EnderecoRead)
def buscar_endereco(endereco_id: int, session: SessionDep):
    """Busca um endereço específico por ID."""
    return endereco_service.buscar(endereco_id, session)


@router.put("/{endereco_id}", response_model=EnderecoRead)
def atualizar_endereco(endereco_id: int, endereco: EnderecoUpdate, session: SessionDep):
    """
    Atualiza os dados de um endereço.
    
    Todos os campos são opcionais - apenas os fornecidos serão atualizados.
    """
    return endereco_service.atualizar(endereco_id, endereco, session)


@router.delete("/{endereco_id}", status_code=status.HTTP_200_OK)
def deletar_endereco(endereco_id: int, session: SessionDep):
    """Deleta um endereço específico."""
    return endereco_service.deletar(endereco_id, session)
