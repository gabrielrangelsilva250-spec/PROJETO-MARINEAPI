from datetime import date
from typing import Optional
from pydantic import BaseModel

class Jogador(BaseModel):
    id_jogador: Optional[int] = None
    nome: str
    ranking: Optional[str] = None
    saldo_de_creditos: Optional[float] = 0.0
    data_de_nascimento: Optional[date] = None
    email: str

    class Config:
        orm_mode = True