from flask import Flask, request

app = Flask(__name__)

# Armazenamento temporário em memória
chamados = []
proximo_id = 1


@app.get("/")
def inicio():
    """Rota inicial da aplicação"""
    return {"mensagem": "API de chamados em funcionamento"}


@app.post("/chamados")
def create_chamados():
    """Salva o chamado"""
    global proximo_id

    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return {"mensagem": "Envie um JSON válido no corpo da requisição"}, 400

    chamado = {
        "id": proximo_id,
        "titulo": dados.get("titulo"),
        "descricao": dados.get("descricao"),
        "solicitante": dados.get("solicitante"),
        "prioridade": dados.get("prioridade"),
        "status": "aberto",
    }
    chamados.append(chamado)
    proximo_id += 1

    return chamado, 201


@app.get("/chamados")
def get_chamados():
    """Lista todos os chamados"""
    return chamados, 200


@app.get("/chamados/<int:chamado_id>")
def get_chamado_by_id(chamado_id):
    """Retorna o chamado que tem id == chamado_id"""
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado, 200
    return {"mensagem": "Chamado não encontrado"}, 404