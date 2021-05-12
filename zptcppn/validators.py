from zptcppn.models import Cartas

def validar_parametros(params):
    excludes = ["id", 
                "__module__", 
                "__doc__", 
                "__tablename__", 
                "_sa_class_manager", 
                "__table__", 
                "__init__", 
                "__mapper__", 
                "data_registro"]
    cartas = list(vars(Cartas))
    
    # https://stackoverflow.com/questions/33577790/exclude-items-from-list-of-lists-python
    cartas = list(set(cartas) - set(excludes))

    page = 1
    limit = 2

    if params:
        page = int(params["page"]) if "page" in params else page
        limit = int(params["limit"]) if "limit" in params else limit
        params.pop("page", None)
        params.pop("limit", None)

        excluir = []

        for _ in params:
            if _ not in cartas:
                excluir.append(_)

        if excluir:
            for _ in excluir:
                params.pop(_, None)
    else:
        params = {}

    return {"pagination": {"page": page, "limit": limit}, "params": params}


def validar_cartas(data):
    erro = []
    campos = ["nome", "texto"]
  
    err = False
    mensagem_obg = "é um campo obrigatório."

    for _ in campos:
        if _ not in data or not data[_]:
            err = True

        if err:
            erro.append(f"['{_}'] {mensagem_obg}")
            err = False

    if not erro:
        return data
    else:
        return erro
