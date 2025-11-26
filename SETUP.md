# 🚀 Setup do Projeto - API Cadastro de Pessoas

## 📋 Pré-requisitos

- Python 3.12+
- Git

## 🔧 Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd api-cadastro-pessoa
```

### 2. Crie o ambiente virtual (recomendado: `.venv`)

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente (opcional)

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite:///./app.db
# Para PostgreSQL: postgresql://user:password@localhost/dbname
# Para MySQL: mysql://user:password@localhost/dbname
```

### 5. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

- **Documentação Swagger**: http://localhost:8000/docs
- **Documentação ReDoc**: http://localhost:8000/redoc

## 📝 Notas Importantes

### ⚠️ Sobre o diretório `Projeto/`

Se você encontrou um diretório chamado `Projeto/` com um ambiente virtual antigo:

1. **NÃO use este ambiente virtual**
2. Ele foi removido do controle de versão
3. Crie um novo ambiente virtual seguindo as instruções acima
4. Você pode deletar o diretório `Projeto/` se desejar:

```powershell
Remove-Item -Recurse -Force Projeto/
```

### 🔄 Migrando do ambiente antigo

Se você estava usando `Projeto/` como ambiente virtual:

1. Desative o ambiente antigo:
   ```powershell
   deactivate
   ```

2. Crie o novo ambiente `.venv` (veja passo 2 acima)

3. Instale as dependências (veja passo 3 acima)

4. Delete o diretório antigo:
   ```powershell
   Remove-Item -Recurse -Force Projeto/
   ```

## 🧪 Testes (em desenvolvimento)

```bash
pytest
pytest --cov=app tests/
```

## 📚 Estrutura do Projeto

```
api-cadastro-pessoa/
├── app/
│   ├── controllers/      # Endpoints da API
│   ├── models/          # Modelos do banco de dados
│   ├── schemas/         # DTOs de validação
│   ├── services/        # Lógica de negócio
│   ├── util/           # Utilitários (database, etc)
│   └── main.py         # Ponto de entrada
├── .venv/              # Ambiente virtual (padrão recomendado)
├── requirements.txt    # Dependências Python
└── README.md          # Documentação principal
```

## 🤝 Contribuindo

1. Crie uma branch para sua feature: `git checkout -b feature/nome-feature`
2. Commit suas mudanças: `git commit -m 'feat: adiciona nova feature'`
3. Push para a branch: `git push origin feature/nome-feature`
4. Abra um Pull Request
