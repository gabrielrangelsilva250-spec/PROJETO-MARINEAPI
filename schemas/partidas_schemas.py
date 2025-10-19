from pydantic import BaseModel
from datetime import datetime

class PartidasSchema(BaseModel):
    id: int
    jogador_id: int
    status: str  # "Em andamento", "finalizada"
    vencedor: str  # "usuario", "ia", "empate"
    iniciado: datetime
    finalizado: datetime

    class Config:
        orm_mode = True
