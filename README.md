# chamados-ads
# API de Chamados de Suporte

**Estudante:** Eduardo Magalhães
**Disciplina:** [ADS0021] Programação para WEB
**Matrícula:** 2025013209
**Atividade:** #2 - Cadastro e Consulta de Chamados

## Objetivo
API de chamados de suporte com Flask, usando uv para gerenciar o ambiente e as dependências. Permite cadastrar, listar e consultar chamados por identificador. Os dados ficam em memória (estruturas Python), então são perdidos quando o servidor é reiniciado. Não há banco de dados nesta etapa.

## Instalação
```bash
uv sync --locked
```

## Execução
```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```
A API fica disponível em `http://localhost:5000`. No GitHub Codespaces, use a URL da porta 5000 encaminhada.

## Endpoints

| Método | Rota             | Descrição                   | Respostas              |
|--------|------------------|-----------------------------|------------------------|
| GET    | `/`              | Rota inicial                | 200                    |
| POST   | `/chamados`      | Cadastra um chamado         | 201                    |
| GET    | `/chamados`      | Lista todos os chamados     | 200                    |
| GET    | `/chamados/{id}` | Consulta um chamado pelo id | 200 (existe) / 404     |

Todas as respostas são em JSON.

### Rota inicial
`GET /` retorna status 200 e o JSON:
```json
{"mensagem": "API de chamados em funcionamento"}
```
Exemplo: `curl -i http://localhost:5000/`

### Cadastrar chamado
`POST /chamados` recebe um JSON com `titulo`, `descricao`, `solicitante` e `prioridade`. A API gera o `id` (inteiro único durante a execução), define o `status` como `aberto` e retorna 201 com o chamado criado.

### Listar chamados
`GET /chamados` retorna 200 e um array com todos os chamados. Sem chamados cadastrados, retorna `[]`.

### Consultar por identificador
`GET /chamados/{id}` retorna 200 e o chamado correspondente. Se o id não existir, retorna 404:
```json
{"mensagem": "Chamado não encontrado"}
```

## Exemplo de cadastro

Requisição:
```bash
curl -X POST http://localhost:5000/chamados \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Impressora sem conexão",
    "descricao": "A impressora do laboratório não aparece na rede.",
    "solicitante": "Ana",
    "prioridade": "media"
  }'
```

Resposta (201 Created):
```json
{
  "id": 1,
  "titulo": "Impressora sem conexão",
  "descricao": "A impressora do laboratório não aparece na rede.",
  "solicitante": "Ana",
  "prioridade": "media",
  "status": "aberto"
}
```