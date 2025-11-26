from typing import TypeVar, Generic, Type, List, Optional
from sqlmodel import Session, select, SQLModel
from fastapi import HTTPException


# Define os TypeVars para os tipos genéricos
ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    Service base genérico para operações CRUD.
    
    Attributes:
        model: Classe do modelo SQLModel
        model_name: Nome do modelo para mensagens de erro
    """
    
    def __init__(self, model: Type[ModelType]):
        self.model = model
        self.model_name = model.__name__
    
    def criar(self, data: CreateSchemaType, session: Session) -> ModelType:
        """
        Cria uma nova instância do modelo.
        
        Args:
            data: Dados para criação
            session: Sessão do banco de dados
            
        Returns:
            Instância criada do modelo
        """
        db_obj = self.model(**data.model_dump())
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
    
    def listar(self, session: Session) -> List[ModelType]:
        """
        Lista todas as instâncias do modelo.
        
        Args:
            session: Sessão do banco de dados
            
        Returns:
            Lista de instâncias do modelo
        """
        return session.exec(select(self.model)).all()
    
    def buscar(self, obj_id: int, session: Session) -> ModelType:
        """
        Busca uma instância do modelo por ID.
        
        Args:
            obj_id: ID da instância
            session: Sessão do banco de dados
            
        Returns:
            Instância encontrada
            
        Raises:
            HTTPException: Se a instância não for encontrada
        """
        obj = session.get(self.model, obj_id)
        if not obj:
            raise HTTPException(
                status_code=404,
                detail=f"{self.model_name} não encontrado(a)"
            )
        return obj
    
    def atualizar(
        self, 
        obj_id: int, 
        data: UpdateSchemaType, 
        session: Session
    ) -> ModelType:
        """
        Atualiza uma instância do modelo.
        
        Args:
            obj_id: ID da instância
            data: Dados para atualização
            session: Sessão do banco de dados
            
        Returns:
            Instância atualizada
            
        Raises:
            HTTPException: Se a instância não for encontrada
        """
        obj = self.buscar(obj_id, session)
        obj_dict = data.model_dump(exclude_unset=True)
        
        for key, value in obj_dict.items():
            setattr(obj, key, value)
        
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
    
    def deletar(self, obj_id: int, session: Session) -> dict:
        """
        Deleta uma instância do modelo.
        
        Args:
            obj_id: ID da instância
            session: Sessão do banco de dados
            
        Returns:
            Mensagem de confirmação
            
        Raises:
            HTTPException: Se a instância não for encontrada
        """
        obj = self.buscar(obj_id, session)
        session.delete(obj)
        session.commit()
        return {"message": f"{self.model_name} deletado(a) com sucesso"}
