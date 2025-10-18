from fastapi import FastAPI, APIRouter
from core.configs import settings

# Importando os routers das APIs
from api.routes.jogadores import router as jogadores_router
from api.routes.jogos import router as jogos_router
from api.routes.pagamento import router as pagamento_router
from api.routes.partidas import router as partidas_router
from api.routes.manutencao import router as manutencao_router
from api.routes.score import router as score_router

# Instância principal da aplicação
app = FastAPI(
    title="MarineAPI 1.0.0",
    version="1.0.0",
    description="API para gerenciamento de partidas, jogadores e navios no jogo Batalha Naval"
)

# Router agrupado para organização
api_router = APIRouter()

# Organização por prefixo e tag
api_router.include_router(jogadores_router, prefix="/jogadores", tags=["Jogadores"])
api_router.include_router(jogos_router, prefix="/jogos", tags=["Jogos"])
api_router.include_router(pagamento_router, prefix="/pagamento", tags=["Pagamento"])
api_router.include_router(partidas_router, prefix="/partidas", tags=["Partidas"])
api_router.include_router(manutencao_router, prefix="/manutencao", tags=["Manutenção"])
api_router.include_router(score_router, prefix="/scores", tags=["Scores"])

# Incluindo o agrupador na aplicação
app.include_router(api_router)

# Execução local com Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
