from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.user import Endereco, Pessoa
from app.schemas.dto import EnderecoCreate, EnderecoUpdate
from app.services.base_service import BaseService


class EnderecoService(BaseService[Endereco, EnderecoCreate, EnderecoUpdate]):
    """
    Service para operações relacionadas a Endereço.
    Herda operações CRUD básicas do BaseService e sobrescreve apenas
    métodos que requerem validações específicas (pessoa existente).
    """
    
    def __init__(self):
        super().__init__(Endereco)
    
    def criar(self, endereco_data: EnderecoCreate, session: Session) -> Endereco:
        """
        Sobrescreve criar() para adicionar validação de pessoa existente.
        
        Args:
            endereco_data: Dados do endereço a ser criado
            session: Sessão do banco de dados
            
        Returns:
            Endereço criado
            
        Raises:
            HTTPException: Se a pessoa não existir
        """
        # Validação específica: pessoa deve existir
        pessoa = session.get(Pessoa, endereco_data.pessoa_id)
        if not pessoa:
            raise HTTPException(
                status_code=400,
                detail="Pessoa informada não existe ou não é válida"
            )
        
        # Chama o método pai para criar
        return super().criar(endereco_data, session)
    
    def listar_por_pessoa(self, pessoa_id: int, session: Session) -> list[Endereco]:
        """
        Lista todos os endereços de uma pessoa específica.
        Método específico que não existe no BaseService.
        
        Args:
            pessoa_id: ID da pessoa
            session: Sessão do banco de dados
            
        Returns:
            Lista de endereços da pessoa
            
        Raises:
            HTTPException: Se a pessoa não for encontrada
        """
        pessoa = session.get(Pessoa, pessoa_id)
        if not pessoa:
            raise HTTPException(
                status_code=404,
                detail="Pessoa não encontrada"
            )
        return pessoa.enderecos

endereco_service = EnderecoService()