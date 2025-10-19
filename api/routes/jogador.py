from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.jogador_schemas import Jogador
from models.jogador_models import JogadorModels
from services.jogador_service import JogadorService
from core.deps import get_db

router = APIRouter(prefix="/jogadores", tags=["Jogadores"])

@router.post("/", response_model=Jogador)
def criar_jogador(jogador: Jogador, db: Session = Depends(get_db)):
    service = JogadorService(db)
    return service.criar_jogador(jogador)

@router.get("/{jogador_id}", response_model=Jogador)
def obter_jogador(jogador_id: int, db: Session = Depends(get_db)):
    service = JogadorService(db)
    jogador = service.buscar_por_id(jogador_id)
    if not jogador:
        raise HTTPException(status_code=404, detail="Jogador não encontrado")
    return jogador


@router.get("/", response_model=list[Jogador])
def listar_jogadores(db: Session = Depends(get_db)):
    service = JogadorService(db)
    return service.listar_todos()
