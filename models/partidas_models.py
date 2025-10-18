from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from core.configs import settings

class partidaModels(settings.DBBaseModel):
    __tablename__ = "Partidas"  # nome da tabela

    id = Column(Integer, primary_key=True, autoincrement=True)  # id único
    jogador_id = Column(Integer, ForeignKey("jogador.id"))
    status = Column(String(20)) #"Em andamento", "finalizada"
    vencedor = Column(String(20)) # "usuario", "ia", "empate"
    iniciado = Column(DateTime, default=datetime.utcnow)
    finalizado = Column(DateTime, default=datetime.utcnow)