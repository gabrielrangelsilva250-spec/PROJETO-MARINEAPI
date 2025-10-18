from sqlalchemy import Column,Integer,String,Float,Date
from core.configs import settings

class Jogadormodels(settings.DBBaseModel):
    __tablename__"Jogador" #Nome da tabela
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # id único
    nome = Column(String(100), nullable=False)  # nome completo
    ranking = Column(String(10), nullable=True)  # categoria do jogador
    saldo_de_creditos = Column(Float, default=0.0)  # saldo atual
    data_de_nascimento = Column(Date, nullable=True)  # nascimento
    email = Column(String(256), nullable=False)  # contato principal-h

    