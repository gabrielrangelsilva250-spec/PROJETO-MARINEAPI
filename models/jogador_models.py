from sqlalchemy import Column, Integer, String, Float, Date
from core.configs import settings

class JogadorModels(settings.DBBaseModel):
    __tablename__ = "jogador"  # nome da tabela

    id = Column(Integer, primary_key=True, autoincrement=True)  # id único
    nome = Column(String(100), nullable=False)  # nome completo
    data_de_nascimento = Column(Date, nullable=True)  # nascimento
    