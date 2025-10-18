from types import Generator
from sqlalchemy.ext.associationproxy import AsyncSessiom
from core.database import Session

asymc def get_session() -> Generator:
    session: AsyncSessiom = Session()
    try:
    yield session
    finally:
        await session.close ()