from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = str(os.getenv("DATABASE_URL"))

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#funcion para abrir y cerrar la bd por cada peticion web que llegue
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()