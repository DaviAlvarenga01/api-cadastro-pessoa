from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.user import Endereco, Pessoa
from app.schemas.dto import EnderecoCreate, EnderecoUpdate

class EnderecoService:
    @staticmethod
    def criar_endereco(endereco_data: EnderecoCreate, session: Session) -> Endereco:
        pessoa = session.get(Pessoa, endereco_data.pessoa_id)
        if not pessoa:
            raise HTTPException(
                status_code=400,
                detail="Pessoa informada não existe ou não é válida"
            )
        db_endereco = Endereco(**endereco_data.model_dump())
        session.add(db_endereco)
        session.commit()
        session.refresh(db_endereco)
        
        return db_endereco
    
    @staticmethod
    def listar_enderecos_pessoa(pessoa_id: int, session: Session) -> list[Endereco]:
        pessoa = session.get(Pessoa, pessoa_id)
        if not pessoa:
            raise HTTPException(
                status_code=404,
                detail="Pessoa não encontrada"
            )
        
        return pessoa.enderecos
    
    @staticmethod
    def buscar_endereco(endereco_id: int, session: Session) -> Endereco:
        endereco = session.get(Endereco, endereco_id)
        if not endereco:
            raise HTTPException(
                status_code=404,
                detail="Endereço não encontrado"
            )
        
        return endereco
    
    @staticmethod
    def atualizar_endereco(
        endereco_id: int, 
        endereco_data: EnderecoUpdate, 
        session: Session
    ) -> Endereco:
        endereco = EnderecoService.buscar_endereco(endereco_id, session)
        endereco_dict = endereco_data.model_dump(exclude_unset=True)
        for key, value in endereco_dict.items():
            setattr(endereco, key, value)
        session.add(endereco)
        session.commit()
        session.refresh(endereco)
        return endereco
    
    @staticmethod
    def deletar_endereco(endereco_id: int, session: Session) -> dict:
        """Deleta um endereço"""
        endereco = EnderecoService.buscar_endereco(endereco_id, session)
        session.delete(endereco)
        session.commit()
        return {"message": "Endereço deletado com sucesso"}