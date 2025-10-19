from sqlalchemy.orm import Session
from models.mensagem_models import MensagemModels
from schemas.mensagem_schemas import MensagemSchemas
from typing import List

class MensagemService:
    def __init__(self, db: Session):
        self.db = db

    def registrar_mensagem(self, dados: MensagemSchemas) -> MensagemModels:
        nova_mensagem = MensagemModels(**dados.model_dump())
        self.db.add(nova_mensagem)
        self.db.commit()
        self.db.refresh(nova_mensagem)
        return nova_mensagem

    def listar_por_partida(self, partida_id: int) -> List[MensagemModels]:
        return self.db.query(MensagemModels).filter_by(partida_id=partida_id).all()
