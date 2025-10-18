from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.mensagem_schemas import MensagemSchema
from services.mensagem_service import MensagemService
from core.deps import get_db

router = APIRouter(prefix="/mensagens", tags=["Mensagens"])

@router.post("/", response_model=MensagemSchema)
async def registrar_mensagem(mensagem: MensagemSchema, db: AsyncSession = Depends(get_db)):
    service = MensagemService(db)
    return await service.registrar_mensagem(mensagem)

@router.get("/partida/{partida_id}", response_model=list[MensagemSchema])
async def listar_mensagens_por_partida(partida_id: int, db: AsyncSession = Depends(get_db)):
    service = MensagemService(db)
    return await service.listar_por_partida(partida_id)
