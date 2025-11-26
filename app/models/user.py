from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class UserBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    email: str = Field(index=True, unique=True)


class EnderecoBase(SQLModel):
    logradouro: str = Field(index=True)
    numero: str = Field(index=True)
    estado: str = Field(max_length=2, index=True)  # UF tem que ser 2 caracteres
    cidade: str = Field(index=True)
    bairro: str = Field(index=True)
    cep: str | None = Field(default=None, max_length=9)  # tem que ser string por causa do '-' e dos zeros à esquerda

class Pessoa(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    enderecos: List["Endereco"] = Relationship(
        back_populates="pessoa",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    
class Endereco(EnderecoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    pessoa_id: int = Field(foreign_key="pessoa.id")
    pessoa: Optional["Pessoa"] = Relationship(back_populates="enderecos")    

