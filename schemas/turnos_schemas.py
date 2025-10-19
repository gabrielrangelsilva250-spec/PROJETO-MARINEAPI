from pydantic import BaseModel
from datetime import datetime

class TurnosSchemas(BaseModel):
    id: int
    partidas_id: int
    jogador: str
    coordenadas: str
    resultado: str
    tempo_jogado: datetime

    class Config:
        from_attributes = True
