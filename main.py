from fastapi import FastAPI
from core.configs import settings

# Importando os routers das APIs
from api.endpoints.jogador_routes import jogador_router
from api.endpoints.mensagem_routes import mensagem_router
from api.endpoints.navio_routes import navio_router
from api.endpoints.partida_routes import partida_router
from api.endpoints.turno_routes import turno_router

app = FastAPI(title="MarineAPI 1.0.0")

# Incluindo os routers na aplicação
app.include_router(jogador_router)
app.include_router(mensagem_router)
app.include_router(navio_router)
app.include_router(partida_router)
app.include_router(turno_router)

# Execução local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)