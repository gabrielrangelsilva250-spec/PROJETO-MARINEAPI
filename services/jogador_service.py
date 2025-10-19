from sqlalchemy.orm import Session
from models.jogador_models import JogadorModels
from schemas.jogador_schemas import Jogador
from typing import Optional

class JogadorService:
    def __init__(self, db: Session):
        self.db = db

    def criar_jogador(self, dados: Jogador) -> JogadorModels:
        novo_jogador = JogadorModels(**dados.dict())
        self.db.add(novo_jogador)
        self.db.commit()
        self.db.refresh(novo_jogador)
        return novo_jogador
