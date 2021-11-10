from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker

SQLALCHAMY_DATABASE_URL = "postgresql://htzeqecigkzlle:4aa44a233f7aa76396fcce7cf873957c323440c3a0cdc4241b09a2d11e5fafeb@ec2-3-227-149-67.compute-1.amazonaws.com:5432/d8iibcolsmi9m7"
engine = create_engine(SQLALCHAMY_DATABASE_URL,echo =True)


SessionLocal = sessionmaker(bind=engine, autoflush= False , autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
