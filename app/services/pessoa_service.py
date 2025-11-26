from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.user import Pessoa
from app.schemas.dto import PessoaCreate, PessoaUpdate
from app.services.base_service import BaseService


class PessoaService(BaseService[Pessoa, PessoaCreate, PessoaUpdate]):
    """
    Service para operações relacionadas a Pessoa.
    Herda operações CRUD básicas do BaseService e adiciona validações específicas.
    """
    
    def __init__(self):
        super().__init__(Pessoa)
    
    def criar_pessoa(self, pessoa_data: PessoaCreate, session: Session) -> Pessoa:
        """
        Cria uma nova pessoa com validação de email único.
        
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
        
        # Usa o método genérico do BaseService
        return self.criar(pessoa_data, session)
    
    def listar_pessoas(self, session: Session) -> list[Pessoa]:
        """Lista todas as pessoas"""
        return self.listar(session)
    
    def buscar_pessoa(self, pessoa_id: int, session: Session) -> Pessoa:
        """Busca pessoa por ID"""
        return self.buscar(pessoa_id, session)
    
    def atualizar_pessoa(
        self, 
        pessoa_id: int, 
        pessoa_data: PessoaUpdate, 
        session: Session
    ) -> Pessoa:
        """
        Atualiza uma pessoa com validação de email único.
        
        Args:
            pessoa_id: ID da pessoa
            pessoa_data: Dados para atualização
            session: Sessão do banco de dados
            
        Returns:
            Pessoa atualizada
            
        Raises:
            HTTPException: Se o email já estiver em uso por outra pessoa
        """
        pessoa = self.buscar_pessoa(pessoa_id, session)
        
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
        
        # Usa o método genérico do BaseService
        return self.atualizar(pessoa_id, pessoa_data, session)
    
    def deletar_pessoa(self, pessoa_id: int, session: Session) -> dict:
        """Deleta uma pessoa"""
        return self.deletar(pessoa_id, session)


# Instância singleton do service
pessoa_service = PessoaService()