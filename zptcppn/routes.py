from flask import request

from zptcppn import app
import zptcppn.queries as q
import zptcppn.validators as v
import zptcppn.serializers as s


@app.route("/")
def index():
    return {"Hello": "World"}


@app.route("/cartas", methods=["GET", "POST"])
def cartas():
    params = request.args.to_dict() if request.args else None
    params = v.validar_parametros(params)

    data = q.listar_cartas(params)
    data = s.obj_cartas(data)

    if request.method == "POST":
        data = request.get_json()
        data = v.validar_cartas(data)

        if type(data) == list:
            return {"erro": data }
            
        data = q.criar_carta(data)
        data = s.obj_carta(data)

        return { "data": data }, 201
    return {"data": data}


@app.route("/cartas/<id>", methods=["GET", "PUT", "DELETE"])
def carta(id):
    if request.method == "PUT":
        data = request.get_json()
        data = v.validar_cartas(data)

        if type(data) == list:
            return {"erro": data }
            
        data = q.atualizar_carta(id, data)
        data = s.obj_carta(data)

        return { "data": data }

    if request.method == "DELETE":
        data = q.apagar_carta(id)
        return {"data": data["mensagem"]}, data["status"]

    data = q.listar_carta(id)
    data = s.obj_carta(data)

    return {"data": data}


