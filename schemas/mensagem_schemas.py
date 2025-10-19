from pydantic import BaseModel
from datetime import datetime

class MensagemSchemas(BaseModel):
    id: int
    partida_id: int
    remetente: str
    conteudo: str
    data_hora: datetime

    class Config:
        from_attributes = True
