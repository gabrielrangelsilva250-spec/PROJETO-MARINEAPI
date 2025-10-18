class TurnoService:
    def __init__(self, db):
        self.db = db

    def registrar_turno(self, dados):
        novo_turno = TurnoModels(**dados.dict())
        self.db.add(novo_turno)
        self.db.commit()
        self.db.refresh(novo_turno)
        return novo_turno

    def listar_por_partida(self, partida_id):
        return self.db.query(TurnoModels).filter_by(partida_id=partida_id).order_by(TurnoModels.tempo_jogado).all()

    def ultimo_turno(self, partida_id):
        return self.db.query(TurnoModels).filter_by(partida_id=partida_id).order_by(TurnoModels.tempo_jogado.desc()).first()
