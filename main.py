from fastapi import FastAPI, APIRouter
from core.configs import settings
from api.routes.jogador import router as jogadores_router
from api.routes.mensagem import router as mensagens_router
from api.routes.navios import router as navios_router
from api.routes.partidas import router as partidas_router
from api.routes.turnos import router as turnos_router

# Instância principal da aplicação
app = FastAPI(
    title="MarineAPI 1.0.0",
    version="1.0.0",
    description="API para gerenciamento de jogadores, navios, mensagens, partidas e turnos no jogo Batalha Naval"
)

# Router agrupado para organização
api_router = APIRouter()

# Organização por prefixo e tag
api_router.include_router(jogadores_router, prefix="/jogadores", tags=["Jogadores"])
api_router.include_router(mensagens_router, prefix="/mensagens", tags=["Mensagens"])
api_router.include_router(navios_router, prefix="/navios", tags=["Navios"])
api_router.include_router(partidas_router, prefix="/partidas", tags=["Partidas"])
api_router.include_router(turnos_router, prefix="/turnos", tags=["Turnos"])

# Incluindo o agrupador na aplicação
app.include_router(api_router)

# Execução local com Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
