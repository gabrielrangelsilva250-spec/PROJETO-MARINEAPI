from fastapi import FastAPI, APIRouter
from core.configs import settings

app = FastAPI (title="MarineAPI 1.0.0")

api_router = APIRouter()

app.include_router(api_router)

if __name__ == "__main__"
import uvicorn
uvicorn.run("maim:app",host="127.0.0.1",port=8000, log_level="info", reload=True)