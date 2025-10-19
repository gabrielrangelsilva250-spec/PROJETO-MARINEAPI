from sqlalchemy.orm import Session
from models.navios_models import NaviosModels
from schemas.navios_schemas import Navio
import json

class NaviosService:
    def __init__(self, db: Session):
        self.db = db

    def criar_navio(self, dados: Navio) -> NaviosModels:
        navio_dict = dados.model_dump()
        navio_dict["coordenadas"] = json.dumps(navio_dict["coordenadas"])  # salva como texto
        novo_navio = NaviosModels(**navio_dict)
        self.db.add(novo_navio)
        self.db.commit()
        self.db.refresh(novo_navio)
        return novo_navio

    def listar_navios(self) -> list[NaviosModels]:
        return self.db.query(NaviosModels).all()

    def buscar_por_id(self, navio_id: int) -> NaviosModels | None:
        return self.db.query(NaviosModels).filter_by(id=navio_id).first()
