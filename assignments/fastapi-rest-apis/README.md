# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e operações CRUD com códigos de resposta adequados.

## 📝 Tarefas

### 🛠️ Iniciar a aplicação FastAPI

#### Descrição
Instale as dependências, execute a aplicação fornecida em `starter-code.py` e crie uma rota inicial para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI disponível na variável `app`.
- Responder a uma requisição `GET /` com uma mensagem indicando que a API está ativa.
- Iniciar com `uvicorn starter-code:app --reload` e disponibilizar a documentação interativa em `/docs`.

### 🛠️ Criar e listar tarefas

#### Descrição
Implemente os endpoints para cadastrar tarefas e consultar a coleção. Mantenha os dados em memória e use modelos Pydantic para validar as informações recebidas.

#### Requisitos
O programa concluído deve:

- Definir um modelo de tarefa com título obrigatório e campos opcionais ou com valor padrão para descrição e conclusão.
- Responder a `GET /tasks` com a lista de tarefas cadastradas.
- Criar tarefas por `POST /tasks`, atribuindo um identificador único e retornando o código HTTP `201`.
- Rejeitar dados inválidos por meio da validação do FastAPI.

### 🛠️ Consultar, atualizar e remover tarefas

#### Descrição
Complete a API permitindo localizar uma tarefa pelo identificador, atualizar somente os campos enviados e remover uma tarefa existente.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para consultar uma tarefa específica.
- Implementar `PATCH /tasks/{task_id}` sem substituir os campos que não foram enviados.
- Implementar `DELETE /tasks/{task_id}` e responder com o código HTTP `204` ao remover uma tarefa.
- Responder com o código HTTP `404` quando o identificador solicitado não existir.
- Permitir testar as rotas pela documentação interativa em `/docs`.
