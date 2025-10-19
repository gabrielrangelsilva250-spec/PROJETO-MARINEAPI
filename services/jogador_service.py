from sqlalchemy.orm import Session
from models.jogador_models import JogadorModels
from schemas.jogador_schemas import Jogador
from typing import Optional

class JogadorService:
    def __init__(self, db: Session):
        self.db = db

    def criar_jogador(self, dados: Jogador) -> JogadorModels:
        novo_jogador = JogadorModels(**dados.model_dump())
        self.db.add(novo_jogador)
        self.db.commit()
        self.db.refresh(novo_jogador)
        return novo_jogador

    def buscar_por_id(self, jogador_id: int) -> Optional[JogadorModels]:
        return self.db.query(JogadorModels).filter_by(id=jogador_id).first()
