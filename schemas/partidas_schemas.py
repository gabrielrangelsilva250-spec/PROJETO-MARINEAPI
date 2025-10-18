from pydantic import BaseModel
from datetime import datetime

class Partida(BaseModel):
    id: int
    jogador_id: int
    status: str  # "Em andamento", "finalizada"
    vencedor: str  # "usuario", "ia", "empate"
    iniciado: datetime
    finalizado: datetime

    class Config:
        orm_mode = True
