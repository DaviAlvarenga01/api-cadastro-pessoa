from fastapi import APIRouter, status
from util.database import SessionDep
from app.schemas.dto import EnderecoCreate, EnderecoRead, EnderecoUpdate
from app.services.endereco_service import EnderecoService

router = APIRouter(prefix="/enderecos", tags=["Endereços"])


@router.post("", response_model=EnderecoRead, status_code=status.HTTP_201_CREATED)
def criar_endereco(endereco: EnderecoCreate, session: SessionDep):
    """
    Cria um novo endereço vinculado a uma pessoa.
    
    - **pessoa_id**: ID da pessoa (deve existir)
    - **logradouro**: Rua, avenida, etc.
    - **numero**: Número do endereço
    - **estado**: UF (2 caracteres)
    - **cidade**: Nome da cidade
    - **bairro**: Nome do bairro
    - **cep**: CEP (opcional)
    """
    return EnderecoService.criar_endereco(endereco, session)


@router.get("/{endereco_id}", response_model=EnderecoRead)
def buscar_endereco(endereco_id: int, session: SessionDep):
    """Busca um endereço específico por ID."""
    return EnderecoService.buscar_endereco(endereco_id, session)


@router.put("/{endereco_id}", response_model=EnderecoRead)
def atualizar_endereco(endereco_id: int, endereco: EnderecoUpdate, session: SessionDep):
    """
    Atualiza os dados de um endereço.
    
    Todos os campos são opcionais - apenas os fornecidos serão atualizados.
    """
    return EnderecoService.atualizar_endereco(endereco_id, endereco, session)


@router.delete("/{endereco_id}", status_code=status.HTTP_200_OK)
def deletar_endereco(endereco_id: int, session: SessionDep):
    """Deleta um endereço específico."""
    return EnderecoService.deletar_endereco(endereco_id, session)
