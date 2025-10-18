from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.mensagem_schema import Mensagem
from models.mensagem_models import MensagemModels
from services.mensagem_service import MensagemService
from core.deps import get_db

router = APIRouter(prefix="/mensagens", tags=["Mensagens"])

@router.post("/", response_model=Mensagem)
def registrar_mensagem(mensagem: Mensagem, db: Session = Depends(get_db)):
    service = MensagemService(db)
    return service.registrar_mensagem(mensagem)

@router.get("/partida/{partida_id}", response_model=list[Mensagem])
def listar_mensagens_por_partida(partida_id: int, db: Session = Depends(get_db)):
    service = MensagemService(db)
    return service.listar_por_partida(partida_id)
