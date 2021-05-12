#### Versão funcional da API: [https://zptcppn.he.ossisnt.dev/](https://zptcppn.he.ossisnt.dev/)

# Observações
Estando ciente das diversas possibilidades de _frameworks_ e bibliotecas existente para a criação de uma API ([Flask-Restful](https://flask-restful.readthedocs.io/en/latest/)/[Plus](https://flask-restplus.readthedocs.io/en/stable/), [FastAPI](https://fastapi.tiangolo.com/), [Django](https://www.djangoproject.com/) com [DRF](https://www.django-rest-framework.org/), etc), a abordagem neste projeto foi um pouco mais "mão na massa" para melhor expor certos conceitos que por vezes são completamente omitidos e acontecem por de baixo dos panos nos exemplos citados acima.

Definitivamente não é um resultado superior, mas é um bom exercício de aprendizado.

# Instruções de Instalação / Uso

Depois de clonar ou baixar os arquivos, para replicar o ambiente deve-se executar os seguintes comandos no terminal:

```sh
python -m venv .venv
.venv\Scripts\Activate (Windows)
source .venv/bin/activate (Linux)
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
Depois de configurado o ambiente, para criar o banco de dados, utilize os seguintes comandos no terminal, na raiz da aplicação:
```python
flask shell
from zptcppn import db, models
db.create_all()
exit()
```
Para iniciar a API, utilize o seguinte comando:
```sh
flask run
```
IMPORTANTE: Durante o desenvolvimento, foi utilizado Python 3.9.2.

Para testar e consumir a API criada, foi utilizado o [Insomnia](https://insomnia.rest/), onde na raiz do repositório já existe um arquivo para importar diretamente na ferramenta com todos os endpoints e estruturas criadas. Outras alternativas como o [Postman](https://www.postman.com/) são completamente funcionais, mas nesta situação o Insomnia seria mais _conveniente_.

# Documentação

#### Visão Geral: Endpoints
|Endpoint|Método|Descrição|
|---|---|---|
|/cartas|GET|Lista todas as cartas|
|/cartas|POST|Cria uma nova carta|
|/cartas/:id|GET|Lista uma carta|
|/cartas/:id|PUT|Atualiza uma carta|
|/cartas/:id|DELETE|Apaga uma carta|


#### Entidade: Carta (POST & PUT)
```json
{
    "nome": "Texto. Campo Obrigatório",
    "texto": "Texto. Campo Obrigatório"
}
```

### Paginação
Há dois parametros para páginação disponíveis:

|Parâmetro|Descrição|
|---|---|
|page|Qualquer número igual ou maior que 1, com base na quantidade de resultados escolhidos.|
|limit|Quantidade máxima de registros retornado por página.|

Exemplo:
```
/cartas?page=2&limit=4
```
Não há a necessidade de utilizá-los em conjunto. Pode-se usar um ou outro, ou ambos.
