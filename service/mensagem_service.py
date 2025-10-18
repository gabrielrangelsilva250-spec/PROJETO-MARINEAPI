class MensagemService:
    def __init__(self, db):
        self.db = db

    def registrar_mensagem(self, dados):
        nova_mensagem = MensagemModels(**dados.dict())
        self.db.add(nova_mensagem)
        self.db.commit()
        self.db.refresh(nova_mensagem)
        return nova_mensagem

    def listar_por_partida(self, partida_id):
        return self.db.query(MensagemModels).filter_by(partida_id=partida_id).all()