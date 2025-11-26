class PessoaCreate(SQLModel):
    nome: str
    email: str

class PessoaRead(SQLModel):
    id: int
    nome: str
    email: str
    enderecos: List[EnderecoRead] = []
    
class PessoaUpdate(SQLModel):
    nome: str | None = None
    email: str | None = None
    
class PessoaDelete(SQLModel):
    id: int
    
class EnderecoCreate(SQLModel):
    logradouro: str
    numero: str
    estado: str
    cidade: str
    bairro: str
    cep: str | None = None
    pessoa_id: int 

class EnderecoUpdate(SQLModel):
    logradouro: str | None = None
    numero: str | None = None
    estado: str | None = None
    cidade: str | None = None
    bairro: str | None = None
    cep: str | None = None


class EnderecoRead(SQLModel):
    id: int
    logradouro: str
    numero: str
    estado: str
    cidade: str
    bairro: str
    cep: str | None
    pessoa_id: int

class EnderecoDelete(SQLModel):
    id: int