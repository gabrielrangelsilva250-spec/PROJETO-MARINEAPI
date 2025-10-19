from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.partidas_schemas import PartidasSchema
from models.partidas_models import PartidasModels
from services.partidas_service import PartidasService
from core.deps import get_db

router = APIRouter(prefix="/partidas", tags=["Partidas"])

@router.post("/", response_model=PartidasSchema)
def criar_partida(partida: PartidasSchema, db: Session = Depends(get_db)):
    service = PartidasService(db)
    return service.criar_partida(partida)

@router.get("/{partida_id}", response_model=PartidasSchema)
def obter_partida(partida_id: int, db: Session = Depends(get_db)):
    service = PartidasService(db)
    partida = service.buscar_partida(partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return partida

@router.get("/", response_model=list[PartidasSchema])
def listar_partidas(db: Session = Depends(get_db)):
    service = PartidasService(db)
    return service.listar_todas()

@router.put("/{partida_id}/finalizar", response_model=PartidasSchema)
def finalizar_partida(partida_id: int, vencedor: str, db: Session = Depends(get_db)):
    service = PartidasService(db)
    partida = service.finalizar_partida(partida_id, vencedor)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return partida
