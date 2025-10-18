from pydantic.v1 import BaseSettings
from sqlachemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1/endpoints"

    DB_URL: str = "mysql + asyncmy://root@127.0.0.1:3306/Marine API"

    DBBaseModel = declarative_base()

    class  config:
        case_sensitive = False
        env+_file ="env"

        settings = Settings()