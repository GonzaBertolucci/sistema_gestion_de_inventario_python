from database import Base, engine
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal

Base.metadata.create_all(bind = engine)

app = FastAPI()

#funcion para abrir y cerrar la bd por cada peticion web que llegue
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/usuarios/", response_model=schemas.Response_usuario)
def crear_usuario(usuario: schemas.Crear_usuario, db: Session = Depends(get_db)):
  nuevo_usuario = models.Usuario(
    nombre_usuario = usuario.nombre_usuario,
    rol_usuario = usuario.rol_usuario,
    contrasenia_usuario = usuario.contrasenia_usuario
  )
  db.add(nuevo_usuario)
  db.commit()
  db.refresh(nuevo_usuario) # La variable no sabe el id asignado, con refresh SQLAlchemy mira la bd y lee el id nuevo y se lo inyecta a la variable
  return nuevo_usuario