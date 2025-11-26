# Services package
from app.services.base_service import BaseService
from app.services.pessoa_service import PessoaService, pessoa_service
from app.services.endereco_service import EnderecoService, endereco_service

__all__ = [
    "BaseService",
    "PessoaService", 
    "pessoa_service",
    "EnderecoService",
    "endereco_service"
]
