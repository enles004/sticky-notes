from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import config

Base = declarative_base()
engine = create_engine(url=config.url_db)

def connection():
    session = scoped_session(sessionmaker(autocommit=False, bind=engine, autoflush=False))
    return session