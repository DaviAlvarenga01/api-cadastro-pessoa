from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.user import Pessoa
from app.schemas.dto import PessoaCreate, PessoaUpdate

class PessoaService:
    @staticmethod
    def criar_pessoa(pessoa_data: PessoaCreate, session: Session) -> Pessoa:
        existing = session.exec(
            select(Pessoa).where(Pessoa.email == pessoa_data.email)
        ).first()
        if existing:
            raise HTTPException(
                status_code=400, 
                detail="Email já está cadastrado"
            )
        db_pessoa = Pessoa(**pessoa_data.model_dump())
        session.add(db_pessoa)
        session.commit()
        session.refresh(db_pessoa)
        return db_pessoa
    
    @staticmethod
    def listar_pessoas(session: Session) -> list[Pessoa]:
        """Lista todas as pessoas"""
        return session.exec(select(Pessoa)).all()
    
    @staticmethod
    def buscar_pessoa(pessoa_id: int, session: Session) -> Pessoa:
        """Busca pessoa por ID"""
        pessoa = session.get(Pessoa, pessoa_id)
        if not pessoa:
            raise HTTPException(
                status_code=404, 
                detail="Pessoa não encontrada"
            )
        return pessoa
    
    @staticmethod
    def atualizar_pessoa(
        pessoa_id: int, 
        pessoa_data: PessoaUpdate, 
        session: Session
    ) -> Pessoa:
        pessoa = PessoaService.buscar_pessoa(pessoa_id, session)
        if pessoa_data.email and pessoa_data.email != pessoa.email:
            existing = session.exec(
                select(Pessoa).where(Pessoa.email == pessoa_data.email)
            ).first()
            
            if existing:
                raise HTTPException(
                    status_code=400,
                    detail="Email já está em uso"
                )
        pessoa_dict = pessoa_data.model_dump(exclude_unset=True)
        for key, value in pessoa_dict.items():
            setattr(pessoa, key, value)
        session.add(pessoa)
        session.commit()
        session.refresh(pessoa)
        return pessoa
    
    @staticmethod
    def deletar_pessoa(pessoa_id: int, session: Session) -> dict:
        pessoa = PessoaService.buscar_pessoa(pessoa_id, session)
        session.delete(pessoa)
        session.commit()
        return {"message": "Pessoa deletada com sucesso"}