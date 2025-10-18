class JogadorService:
    def __init__(self, db):
        self.db = db

    def criar_jogador(self, dados):
        novo_jogador = JogadorModels(**dados.dict())
        self.db.add(novo_jogador)
        self.db.commit()
        self.db.refresh(novo_jogador)
        return novo_jogador

    def buscar_por_id(self, jogador_id):
        return self.db.query(JogadorModels).filter_by(id=jogador_id).first()

    def listar_todos(self):
        return self.db.query(JogadorModels).all()
