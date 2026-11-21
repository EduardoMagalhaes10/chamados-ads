# chamados-ads
# API de Chamados de Suporte

**Estudante:** Eduardo Magalhães
**Disciplina:** [ADS0021] Programação para WEB
**Matrícula:** 2025013209

## Objetivo
Estrutura inicial de uma API de chamados de suporte com Flask, usando uv para gerenciar o ambiente e as dependências.

## Instalação
```bash
uv sync --locked
```

## Execução
```bash
uv run flask --app app run --host=0.0.0.0 --port=5000
```

## Rota inicial
`GET /` retorna status 200 e o JSON:
```json
{"mensagem": "API de chamados em funcionamento"}
```
Exemplo: `curl -i http://localhost:5000/`