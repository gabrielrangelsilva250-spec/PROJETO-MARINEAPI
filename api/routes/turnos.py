from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.turnos_schemas import TurnosSchema
from models.turnos_models import TurnosModels
from services.turnos_service import TurnosService
from core.deps import get_db

router = APIRouter(prefix="/turnos", tags=["Turnos"])

@router.post("/", response_model=Turno)
def registrar_turno(turno: Turno, db: Session = Depends(get_db)):
    service = TurnoService(db)
    return service.registrar_turno(turno)

@router.get("/partida/{partida_id}", response_model=list[Turno])
def listar_turnos_por_partida(partida_id: int, db: Session = Depends(get_db)):
    service = TurnoService(db)
    return service.listar_por_partida(partida_id)

@router.get("/partida/{partida_id}/ultimo", response_model=Turno)
def obter_ultimo_turno(partida_id: int, db: Session = Depends(get_db)):
    service = TurnoService(db)
    turno = service.ultimo_turno(partida_id)
    if not turno:
        raise HTTPException(status_code=404, detail="Nenhum turno encontrado")
    return turno
