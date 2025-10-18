from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from core.configs import settings

id = Column(Integer, primary_key=True)
partida_id = Column(Integer, ForeignKey("partidas.id"))
remetente = Column(String(20))  # "usuario" ou "ia"
conteudo = Column(Text)
data_hora = Column(DateTime, default=datetime.utcnow)
