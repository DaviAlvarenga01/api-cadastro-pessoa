# API de Cadastro de Pessoas

API RESTful desenvolvida com FastAPI para gerenciar cadastro de pessoas e seus endereços.

## ✨ Features

- ✅ CRUD completo de Pessoas
- ✅ CRUD completo de Endereços
- ✅ Relacionamento 1:N (Pessoa → Endereços)
- ✅ Validações robustas (email, CEP, UF)
- ✅ Documentação automática (Swagger/ReDoc)
- ✅ Arquitetura em camadas (Controller → Service → Model)
- ✅ Uso de Generics para reutilização de código
- ✅ SQLModel com SQLite (fácil migração para PostgreSQL/MySQL)

## 🚀 Quick Start

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd api-cadastro-pessoa

# Crie ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
# source .venv/bin/activate  # Linux/Mac

# Instale dependências
pip install -r requirements.txt

# Execute
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs

## 📖 Documentação Completa

Veja [SETUP.md](SETUP.md) para instruções detalhadas de instalação e configuração.

## 🏗️ Arquitetura

```
app/
├── controllers/  # Rotas e endpoints HTTP
├── services/     # Lógica de negócio (+ BaseService genérico)
├── models/       # Modelos SQLModel (ORM)
├── schemas/      # DTOs Pydantic (validação)
└── util/         # Database connection e utilitários
```

## 🔗 Endpoints Principais

### Pessoas
- `POST /pessoas` - Criar pessoa
- `GET /pessoas` - Listar todas
- `GET /pessoas/{id}` - Buscar por ID
- `PUT /pessoas/{id}` - Atualizar
- `DELETE /pessoas/{id}` - Deletar
- `GET /pessoas/{id}/enderecos` - Listar endereços da pessoa

### Endereços
- `POST /enderecos` - Criar endereço
- `GET /enderecos/{id}` - Buscar por ID
- `PUT /enderecos/{id}` - Atualizar
- `DELETE /enderecos/{id}` - Deletar

## 🛠️ Stack Tecnológica

- **FastAPI** - Framework web moderno e rápido
- **SQLModel** - ORM com integração Pydantic
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI de alta performance
- **SQLite** - Banco de dados (dev) - facilmente substituível

## 📝 Exemplo de Uso

```python
# Criar pessoa
POST /pessoas
{
  "nome": "João Silva",
  "idade": 30,
  "email": "joao@email.com"
}

# Criar endereço
POST /enderecos
{
  "logradouro": "Rua das Flores",
  "numero": "123",
  "estado": "sp",  # Auto-convertido para "SP"
  "cidade": "São Paulo",
  "bairro": "Centro",
  "cep": "12345-678",
  "pessoa_id": 1
}
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [SETUP.md](SETUP.md) para instruções de desenvolvimento.

## 📄 Licença

[Adicionar licença]