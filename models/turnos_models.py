from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from core.configs import settings

class TurnosModels(settings.DBBaseModel):
    __tablename__ = "Turno" #nome da tabela
id = Column(Integer, primary_key=True)
partidas_id= Column (Integer, ForeignKey("partidas.id"))
jogador= Column(String(20)) 
coordenadas = Column(String(5))
resultado = Column(String(20))
tempo_jogado = Column(DateTime, default=datetime.utcnow)
