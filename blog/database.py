from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker

SQLALCHAMY_DATABASE_URL = "postgres://stcfrdskwngtzz:480feb19c356fb542e5fc38ee95fabf0b55e06a224649b7ecde8653d820e444e@ec2-52-86-177-34.compute-1.amazonaws.com:5432/d8he5lvhbhonhn"
engine = create_engine(SQLALCHAMY_DATABASE_URL,echo =True)


SessionLocal = sessionmaker(bind=engine, autoflush= False , autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
