from fastapi import FastAPI, APIRouter
from core.configs import settings
from api.endpoints.jogador_routes import jogador_router
from api.endpoints.mensagem_routes import mensagem_router
from api.endpoints.navio_routes import navio_router
from api.endpoints.partida_routes import partida_router
from api.endpoints.turno_routes import turno_router

app = FastAPI (title="MarineAPI 1.0.0")


api_router = APIRouter()

app.include_router(api_router)

if __name__ == "__main__"
import uvicorn
uvicorn.run("maim:app",host="127.0.0.1",port=8000, log_level="info", reload=True)