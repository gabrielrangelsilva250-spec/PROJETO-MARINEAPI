from sqlalchemy.orm import Session
from typing import Optional
from models.partidas_models import PartidasModels
from schemas.partidas_schemas import PartidasSchema

class PartidasService:
    def __init__(self, db: Session):
        self.db = db

    def criar_partida(self, partida_data: PartidasSchema) -> PartidasModels:
        nova_partida = PartidasModels(**partida_data.dict())
        self.db.add(nova_partida)
        self.db.commit()
        self.db.refresh(nova_partida)
        return nova_partida

    def buscar_partida(self, partida_id: int) -> Optional[PartidasModels]:
        return self.db.query(PartidasModels).filter_by(id=partida_id).first()
