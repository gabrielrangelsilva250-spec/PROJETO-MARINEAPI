from pydantic import BaseModel
from datetime import datetime

class Turno(BaseModel):
    id: int
    partidas_id: int
    jogador: str
    coordenadas: str
    resultado: str
    tempo_jogado: datetime

    class Config:
        orm_mode = True
