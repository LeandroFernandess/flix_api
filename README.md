# API de Filmes 🎬

Uma API RESTful desenvolvida em **Django** e **Django REST Framework** para gerenciamento de filmes, atores, gênros e reviews. A aplicação permite criar, visualizar, editar e excluir registros relacionados a filmes, oferecendo um painel administrativo e endpoints prontos para integração.

## Tecnologias Utilizadas 🛠️

- **Django**: Framework web principal.
- **Django REST Framework (DRF)**: Facilita a criação de APIs RESTful.
- **Python**: Linguagem de programação principal.
- **SQLite**: Banco de dados utilizado em desenvolvimento.
- **Django Admin**: Interface administrativa nativa do Django.
- **Markdown**: Para documentação (`documentos.md`).

---

## Estrutura do Projeto 📂

A estrutura do projeto está organizada da seguinte forma:

```bash
filme-api/
├── actors/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── authentication/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── genres/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── movies/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── reviews/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── manage.py              # Gerenciador de comandos do Django
├── requirements.txt       # Dependências do projeto
├── requirements_dev.txt   # Dependências para ambiente de desenvolvimento
```

---

## Funcionalidades 🚀

- **Autenticação**:
  - Registro e login de usuários.
  - Geração de tokens para segurança da API.

- **Módulo Filmes**:
  - CRUD completo para gerenciamento de filmes.
  - Relacionamento com gênros, atores e reviews.

- **Módulo Atores**:
  - Cadastro de atores com dados relevantes (nome, bio, data de nascimento).

- **Módulo Gênros**:
  - Adição e gerenciamento de gênros de filmes.

- **Módulo Reviews**:
  - Usuários podem adicionar reviews a filmes.
  - Controle de avaliações com base no usuário autenticado.

- **API RESTful**:
  - Endpoints documentados com **Django REST Framework**.
  - Respostas estruturadas em JSON.

- **Django Admin**:
  - Painel administrativo integrado para gerenciamento de dados.

---

## Como Executar o Projeto 🔧

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/filme-api.git
   ```

2. **Entre no diretório do projeto**:
   ```bash
   cd filme-api
   ```

3. **Crie e ative o ambiente virtual**:
   ```bash
   python -m venv venv
   # No Windows
   venv\Scripts\activate
   # No Unix ou MacOS
   source venv/bin/activate
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Realize as migrações do banco de dados**:
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário para o Django Admin**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

8. **Acesse o projeto**:
   - Admin: `http://127.0.0.1:8000/admin`
   - API: `http://127.0.0.1:8000/` (ver endpoints disponíveis).

## Endpoints Principais 🌐

| Recurso          | Método  | URL                       | Descrição                   |
|------------------|---------|---------------------------|-----------------------------|
| **Filmes**       | GET     | `/api/movies/`            | Lista todos os filmes       |
|                  | POST    | `/api/movies/`            | Cria um novo filme          |
|                  | GET     | `/api/movies/{id}/`       | Detalhe de um filme         |
|                  | PUT     | `/api/movies/{id}/`       | Atualiza um filme           |
|                  | DELETE  | `/api/movies/{id}/`       | Remove um filme             |
| **Atores**       | GET     | `/api/actors/`            | Lista todos os atores       |
|                  | POST    | `/api/actors/`            | Cria um novo ator           |
|                  | GET     | `/api/actors/{id}/`       | Detalhe de um ator          |
|                  | PUT     | `/api/actors/{id}/`       | Atualiza um ator            |
|                  | DELETE  | `/api/actors/{id}/`       | Remove um ator              |
| **Gêneros**      | GET     | `/api/genres/`            | Lista todos os gêneros      |
|                  | POST    | `/api/genres/`            | Cria um novo gênero         |
|                  | GET     | `/api/genres/{id}/`       | Detalhe de um gênero        |
|                  | PUT     | `/api/genres/{id}/`       | Atualiza um gênero          |
|                  | DELETE  | `/api/genres/{id}/`       | Remove um gênero            |
| **Reviews**      | GET     | `/api/reviews/`           | Lista todas as reviews      |
|                  | POST    | `/api/reviews/`           | Cria uma nova review        |
|                  | GET     | `/api/reviews/{id}/`      | Detalhe de uma review       |
|                  | PUT     | `/api/reviews/{id}/`      | Atualiza uma review         |
|                  | DELETE  | `/api/reviews/{id}/`      | Remove uma review           |

---

## Autenticação 🔐

A autenticação é feita via **Token** (JWT). Para acessar endpoints protegidos:

1. Obtenha um token enviando um POST para:
   ```bash
   /api/auth/login/
   ```
   - **Body**: `{ "username": "seu-usuario", "password": "sua-senha" }`

2. Use o token nos headers:
   ```
   Authorization: Bearer <seu_token>
   ```

---

## Contato 💬

Caso tenha dúvidas ou sugestões, entre em contato:

- **Nome**: Leandro Fernandes
- **Email**: leandrofernandes1600@gmail.com
- **GitHub**: https://github.com/LeandroFernandess

---

*Documentação atualizada em: `17/12/2024`.* 🚀

