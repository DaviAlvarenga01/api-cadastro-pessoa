from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class PessoaBase(SQLModel):
    """Classe base para Pessoa com campos comuns."""
    nome: str = Field(min_length=3, max_length=200)
    idade: int | None = Field(default=None, ge=0, le=150)
    email: str = Field(unique=True, max_length=255)


class EnderecoBase(SQLModel):
    """Classe base para Endereço com campos comuns."""
    logradouro: str = Field(min_length=3, max_length=200)
    numero: str = Field(max_length=10)
    estado: str = Field(min_length=2, max_length=2, regex=r'^[A-Z]{2}$')  # UF tem que ser 2 caracteres maiúsculas
    cidade: str = Field(min_length=2, max_length=100)
    bairro: str = Field(min_length=2, max_length=100)
    cep: str | None = Field(default=None, max_length=9, regex=r'^\d{5}-?\d{3}$')  # Formato: 12345-678 ou 12345678

class Pessoa(PessoaBase, table=True):
    """Modelo de tabela Pessoa no banco de dados."""
    id: int | None = Field(default=None, primary_key=True)
    pai_id: int | None = Field(default=None, foreign_key="pessoa.id", index=True)
    
    enderecos: List["Endereco"] = Relationship(
        back_populates="pessoa",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    pai: Optional["Pessoa"] = Relationship(
        back_populates="filhos",
        sa_relationship_kwargs={"remote_side": "Pessoa.id"}
    )
    filhos: List["Pessoa"] = Relationship(back_populates="pai")
    
class Endereco(EnderecoBase, table=True):
    """Modelo de tabela Endereco no banco de dados."""
    id: int | None = Field(default=None, primary_key=True)
    pessoa_id: int = Field(foreign_key="pessoa.id", index=True)
    pessoa: Optional["Pessoa"] = Relationship(back_populates="enderecos")    

