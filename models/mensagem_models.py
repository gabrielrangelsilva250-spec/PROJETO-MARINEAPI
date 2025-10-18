from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from core.configs import settings

class Mensagemmodels(settings.DBBaseModel):
    __tablename__"Mensagens"#Nome da tabela no banco de dados
id = Column(Integer, primary_key=True)
partida_id = Column(Integer, ForeignKey("partidas.id"))
remetente = Column(String(20))  # "usuario" ou "ia"
conteudo = Column(Text)
data_hora = Column(DateTime, default=datetime.utcnow)
