from pydantic import BaseModel
from typing import List
from datetime import datetime

class Navio(BaseModel):
    id: int
    jogador: str  # "usuario" ou "ia"
    tipo: str     # "porta-aviões", "submarino", etc.
    coordenadas: str  # Ex: "A1,A2,A3"
    afundado: bool

    class Config:
        orm_mode = True
