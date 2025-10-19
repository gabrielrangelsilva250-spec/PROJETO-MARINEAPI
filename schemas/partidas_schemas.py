from pydantic import BaseModel
from datetime import datetime

class PartidasSchema(BaseModel):
    id: int
    jogador_id: int
    status: str
    vencedor: str
    iniciado: datetime
    finalizado: datetime

    class Config:
        from_attributes = True
