from sqlalchemy import Column, Integer, String, Text
from core.configs import settings

class NaviosModels(settings.DBBaseModel):
    __tablename__ = "Navio"  # nome da tabela

    id = Column(Integer, primary_key=True)
    jogador = Column(String(20))  # "usuario" ou "ia"
    tipo = Column(String(20))  # "porta-aviões", "submarino", etc.
    coordenadas = Column(Text)  # Lista de coordenadas ocupadas