from pydantic import BaseModel
from datetime import datetime

class MensagemSchemas(BaseModel):
    id: int
    partida_id: int
    remetente: str  # "usuario" ou "ia"
    conteudo: str
    data_hora: datetime

    class Config:
        orm_mode = True
