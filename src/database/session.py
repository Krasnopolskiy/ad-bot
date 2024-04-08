from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config.database import DatabaseSettings


class DatabaseSessionManager:
    engine = create_engine(url=DatabaseSettings().url)

    def __init__(self):
        database_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.session = database_session()

    def __enter__(self) -> Session:
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
