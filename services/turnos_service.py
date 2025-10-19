from sqlalchemy.orm import Session
from models.turnos_models import TurnosModels
from schemas.turnos_schemas import TurnosSchemas
from typing import List

class TurnosService:
    def __init__(self, db: Session):
        self.db = db

    def registrar_turno(self, dados: TurnosSchemas) -> TurnosModels:
        novo_turno = TurnosModels(**dados.model_dump())
        self.db.add(novo_turno)
        self.db.commit()
        self.db.refresh(novo_turno)
        return novo_turno

    def listar_por_partida(self, partida_id: int) -> List[TurnosModels]:
        return self.db.query(TurnosModels).filter_by(partidas_id=partida_id).all()

    def ultimo_turno(self, partida_id: int) -> TurnosModels | None:
        return (
            self.db.query(TurnosModels)
            .filter_by(partidas_id=partida_id)
            .order_by(TurnosModels.tempo_jogado.desc())
            .first()
        )
