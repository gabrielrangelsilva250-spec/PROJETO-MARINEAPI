from datetime import date
from typing import Optional
from pydantic import BaseModel

class Jogador(BaseModel):
    id_jogador: Optional[int] = None
    nome: str
    data_de_nascimento: Optional[date] = None

    class Config:
        from_attributes = True
