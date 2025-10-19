from pydantic import BaseModel
from typing import List

class Navio(BaseModel):
    id: int
    jogador: str
    tipo: str
    coordenadas: List[str]

    class Config:
        from_attributes = True
