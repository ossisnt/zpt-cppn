from flask import request

def obj_carta(data):
    obj = {
        "id": data.id,
        "nome": data.nome,
        "texto": data.texto,
        "data_registro": data.data_registro,
        "url": f'{request.url_root}cartas/{data.id}'
    }
        
    return obj


def obj_cartas(data):
    lista = []
    
    for obj in data:
        lista.append(obj_carta(obj))

    return lista
