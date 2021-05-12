from zptcppn import db
from datetime import datetime as dt

class Cartas(db.Model):
    id = db.Column(db.String(), primary_key=True, unique=True)
    nome = db.Column(db.String(), nullable=False)
    texto = db.Column(db.Text(), nullable=False)
    data_registro = db.Column(db.DateTime, nullable=False, default=dt.utcnow)

    def __repr__(self):
        return f'{self.nome}, {self.data_registro}'

