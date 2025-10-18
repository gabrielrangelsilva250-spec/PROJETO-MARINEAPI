class NavioService:
    def __init__(self, db):
        self.db = db

    def posicionar_navio(self, dados):
        novo_navio = NaviosModels(**dados.dict())
        self.db.add(novo_navio)
        self.db.commit()
        self.db.refresh(novo_navio)
        return novo_navio

    def listar_por_jogador(self, partida_id, jogador):
        return self.db.query(NaviosModels).filter_by(partida_id=partida_id, jogador=jogador).all()

    def verificar_afundado(self, navio_id):
        navio = self.db.query(NaviosModels).filter_by(id=navio_id).first()
        return navio.afundado if navio else None
