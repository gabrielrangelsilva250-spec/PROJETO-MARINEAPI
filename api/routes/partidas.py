from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.partidas_schema import PartidaSchema
from models.partidas_models import PartidaModels
from services.partidas_service import PartidaService
from core.deps import get_db

router = APIRouter(prefix="/partidas", tags=["Partidas"])

@router.post("/", response_model=Partida)
def criar_partida(partida: Partida, db: Session = Depends(get_db)):
    service = PartidaService(db)
    return service.criar_partida(partida)

@router.get("/{partida_id}", response_model=Partida)
def obter_partida(partida_id: int, db: Session = Depends(get_db)):
    service = PartidaService(db)
    partida = service.buscar_por_id(partida_id)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return partida

@router.get("/", response_model=list[Partida])
def listar_partidas(db: Session = Depends(get_db)):
    service = PartidaService(db)
    return service.listar_todas()

@router.put("/{partida_id}/finalizar", response_model=Partida)
def finalizar_partida(partida_id: int, vencedor: str, db: Session = Depends(get_db)):
    service = PartidaService(db)
    partida = service.finalizar_partida(partida_id, vencedor)
    if not partida:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return partida
