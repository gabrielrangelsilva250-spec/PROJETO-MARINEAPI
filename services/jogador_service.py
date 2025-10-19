from sqlalchemy.ext.asyncio import AsyncSession
from models.jogador_models import JogadorModels
from schemas.jogador_schemas import Jogador
from typing import Optional
from sqlalchemy import select

class JogadorService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def criar_jogador(self, dados: Jogador) -> JogadorModels:
        novo_jogador = JogadorModels(**dados.model_dump())
        self.db.add(novo_jogador)
        await self.db.commit()
        await self.db.refresh(novo_jogador)
        return novo_jogador

    async def buscar_por_id(self, jogador_id: int) -> Optional[JogadorModels]:
        result = await self.db.execute(
            select(JogadorModels).filter_by(id=jogador_id)
        )
        return result.scalar_one_or_none()
