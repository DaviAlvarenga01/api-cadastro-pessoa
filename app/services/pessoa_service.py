from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.user import Pessoa
from app.schemas.dto import PessoaCreate, PessoaUpdate
from app.services.base_service import BaseService


class PessoaService(BaseService[Pessoa, PessoaCreate, PessoaUpdate]):
    """
    Service para operações relacionadas a Pessoa.
    Herda operações CRUD básicas do BaseService e sobrescreve apenas
    métodos que requerem validações específicas (email único).
    """
    
    def __init__(self):
        super().__init__(Pessoa)
    
    def criar(self, pessoa_data: PessoaCreate, session: Session) -> Pessoa:
        """
        Sobrescreve criar() para adicionar validação de email único.
        
        Args:
            pessoa_data: Dados da pessoa a ser criada
            session: Sessão do banco de dados
            
        Returns:
            Pessoa criada
            
        Raises:
            HTTPException: Se o email já estiver cadastrado
        """
        # Validação específica: email único
        existing = session.exec(
            select(Pessoa).where(Pessoa.email == pessoa_data.email)
        ).first()
        if existing:
            raise HTTPException(
                status_code=400, 
                detail="Email já está cadastrado"
            )
        
        # Chama o método pai para criar
        return super().criar(pessoa_data, session)
    
    def atualizar(
        self, 
        pessoa_id: int, 
        pessoa_data: PessoaUpdate, 
        session: Session
    ) -> Pessoa:
        """
        Sobrescreve atualizar() para adicionar validação de email único.
        
        Args:
            pessoa_id: ID da pessoa
            pessoa_data: Dados para atualização
            session: Sessão do banco de dados
            
        Returns:
            Pessoa atualizada
            
        Raises:
            HTTPException: Se o email já estiver em uso por outra pessoa
        """
        pessoa = self.buscar(pessoa_id, session)
        
        # Validação específica: email único ao atualizar
        if pessoa_data.email and pessoa_data.email != pessoa.email:
            existing = session.exec(
                select(Pessoa).where(Pessoa.email == pessoa_data.email)
            ).first()
            
            if existing:
                raise HTTPException(
                    status_code=400,
                    detail="Email já está em uso"
                )
        
        # Chama o método pai para atualizar
        return super().atualizar(pessoa_id, pessoa_data, session)


# Instância singleton do service
pessoa_service = PessoaService()