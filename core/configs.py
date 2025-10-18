from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base
from typing import ClassVar

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1/endpoints"
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/marine_api"

    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = False
        env_file = ".env"

settings = Settings()

