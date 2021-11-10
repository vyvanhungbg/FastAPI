from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
import config
SQLALCHAMY_DATABASE_URL = config.Settings.POSTGRES_DB_URL
engine = create_engine(SQLALCHAMY_DATABASE_URL,echo =True)


SessionLocal = sessionmaker(bind=engine, autoflush= False , autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
