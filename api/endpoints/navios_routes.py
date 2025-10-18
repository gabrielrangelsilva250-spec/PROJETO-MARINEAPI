from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.navio_schema import NavioSchema
from models.navio_models import NaviosModels
from services.navio_service import NavioService
from core.deps import get_db

router = APIRouter(prefix="/navios", tags=["Navios"])

@router.post("/", response_model=Navio)
def posicionar_navio(navio: Navio, db: Session = Depends(get_db)):
    service = NavioService(db)
    return service.posicionar_navio(navio)

@router.get("/partida/{partida_id}/jogador/{jogador}", response_model=list[Navio])
def listar_navios_por_jogador(partida_id: int, jogador: str, db: Session = Depends(get_db)):
    service = NavioService(db)
    return service.listar_por_jogador(partida_id, jogador)

@router.get("/{navio_id}/afundado", response_model=bool)
def verificar_afundado(navio_id: int, db: Session = Depends(get_db)):
    service = NavioService(db)
    status = service.verificar_afundado(navio_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Navio não encontrado")
    return status
