from uuid import uuid4

from zptcppn import db
from zptcppn.models import Cartas


def criar_carta(data):
    carta = Cartas(
        id = uuid4().hex,
        nome = data["nome"].strip(),
        texto = data["texto"].strip()
    )

    db.session.add(carta)
    db.session.commit()

    return carta


def apagar_carta(data):
    try:
        carta = Cartas.query.filter_by(id=data).first_or_404()
        db.session.delete(carta)
        db.session.commit()
        status = {"mensagem": "", "status": 200}  
    except:
        status = {"mensagem": "", "status": 204}

    return status


def listar_cartas(params):
    cartas = Cartas.query.filter_by(**params["params"])\
        .paginate(page=params["pagination"]["page"], max_per_page=params["pagination"]["limit"], error_out=False)
    
    return cartas.items


def listar_carta(data):
    carta = Cartas.query.filter_by(id=data).first_or_404()
    return carta


def atualizar_carta(id, data):
    carta = Cartas.query.filter_by(id=id).first_or_404()

    carta.nome = data["nome"] if data["nome"] != carta.nome else carta.nome
    carta.texto = data["texto"] if data["texto"] != carta.texto else carta.texto

    db.session.commit()

    return carta
