from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

DB_HOST = "localhost"
DB_NAME = "FastAPI_DB"
DB_USER = "omar"
DB_PASSWORD = "omar123"
DB_PORT = 5432

URL_DATABASE = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
