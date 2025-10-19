class PartidasService:
    def __init__(self, db: Session):
        self.db = db

    def criar_partida(self, partida_data: PartidaCreate) -> PartidaModels:
        nova_partida = PartidaModels(**partida_data.dict())
        self.db.add(nova_partida)
        self.db.commit()
        self.db.refresh(nova_partida)
        return nova_partida

    def buscar_partida(self, partida_id: int) -> Optional[PartidaModels]:
        return self.db.query(PartidaModels).filter_by(id=partida_id).first()
