from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.user import Endereco, Pessoa
from app.schemas.dto import EnderecoCreate, EnderecoUpdate
from app.services.base_service import BaseService


class EnderecoService(BaseService[Endereco, EnderecoCreate, EnderecoUpdate]):
    """
    Service para operações relacionadas a Endereço.
    Herda operações CRUD básicas do BaseService e adiciona validações específicas.
    """
    
    def __init__(self):
        super().__init__(Endereco)
    
    def criar_endereco(self, endereco_data: EnderecoCreate, session: Session) -> Endereco:
        """
        Cria um novo endereço com validação de pessoa existente.
        
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
        return self.criar(endereco_data, session)
    
    def listar_enderecos_pessoa(self, pessoa_id: int, session: Session) -> list[Endereco]:
        """
        Lista todos os endereços de uma pessoa específica.
        
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
    
    def buscar_endereco(self, endereco_id: int, session: Session) -> Endereco:
        """Busca um endereço por ID"""
        return self.buscar(endereco_id, session)
    
    def atualizar_endereco(
        self, 
        endereco_id: int, 
        endereco_data: EnderecoUpdate, 
        session: Session
    ) -> Endereco:
        """Atualiza um endereço"""
        return self.atualizar(endereco_id, endereco_data, session)
    
    def deletar_endereco(self, endereco_id: int, session: Session) -> dict:
        """Deleta um endereço"""
        return self.deletar(endereco_id, session)

endereco_service = EnderecoService()