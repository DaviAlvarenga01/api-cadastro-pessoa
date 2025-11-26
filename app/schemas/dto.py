from sqlmodel import SQLModel, Field
from typing import List
from pydantic import EmailStr, field_validator


class PessoaCreate(SQLModel):
    """Schema para criação de Pessoa."""
    nome: str = Field(min_length=3, max_length=200, description="Nome completo da pessoa")
    idade: int | None = Field(default=None, ge=0, le=150, description="Idade da pessoa")
    email: EmailStr = Field(description="Email válido e único")
    
    @field_validator('nome')
    @classmethod
    def validar_nome(cls, v: str) -> str:
        """Valida que o nome não contém apenas espaços."""
        if not v.strip():
            raise ValueError('Nome não pode ser vazio ou conter apenas espaços')
        return v.strip()

class PessoaRead(SQLModel):
    """Schema para leitura de Pessoa."""
    id: int
    nome: str
    idade: int | None = None
    email: str
    enderecos: List['EnderecoRead'] = []
    
class PessoaUpdate(SQLModel):
    """Schema para atualização de Pessoa."""
    nome: str | None = Field(default=None, min_length=3, max_length=200)
    idade: int | None = Field(default=None, ge=0, le=150)
    email: EmailStr | None = None
    
    @field_validator('nome')
    @classmethod
    def validar_nome(cls, v: str | None) -> str | None:
        """Valida que o nome não contém apenas espaços."""
        if v is not None and not v.strip():
            raise ValueError('Nome não pode conter apenas espaços')
        return v.strip() if v else None


class EnderecoCreate(SQLModel):
    """Schema para criação de Endereço."""
    logradouro: str = Field(min_length=3, max_length=200, description="Logradouro (rua, avenida, etc)")
    numero: str = Field(max_length=10, description="Número do endereço")
    estado: str = Field(min_length=2, max_length=2, regex=r'^[A-Z]{2}$', description="UF (ex: SP, RJ)")
    cidade: str = Field(min_length=2, max_length=100, description="Nome da cidade")
    bairro: str = Field(min_length=2, max_length=100, description="Nome do bairro")
    cep: str | None = Field(default=None, max_length=9, regex=r'^\d{5}-?\d{3}$', description="CEP (ex: 12345-678)")
    pessoa_id: int = Field(gt=0, description="ID da pessoa proprietária")
    
    @field_validator('estado')
    @classmethod
    def validar_estado(cls, v: str) -> str:
        """Converte estado para maiúsculas."""
        return v.upper() 

class EnderecoUpdate(SQLModel):
    """Schema para atualização de Endereço."""
    logradouro: str | None = Field(default=None, min_length=3, max_length=200)
    numero: str | None = Field(default=None, max_length=10)
    estado: str | None = Field(default=None, min_length=2, max_length=2, regex=r'^[A-Z]{2}$')
    cidade: str | None = Field(default=None, min_length=2, max_length=100)
    bairro: str | None = Field(default=None, min_length=2, max_length=100)
    cep: str | None = Field(default=None, max_length=9, regex=r'^\d{5}-?\d{3}$')
    
    @field_validator('estado')
    @classmethod
    def validar_estado(cls, v: str | None) -> str | None:
        """Converte estado para maiúsculas."""
        return v.upper() if v else None


class EnderecoRead(SQLModel):
    """Schema para leitura de Endereço."""
    id: int
    logradouro: str
    numero: str
    estado: str
    cidade: str
    bairro: str
    cep: str | None
    pessoa_id: int