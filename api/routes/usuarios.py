from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import schemas
from models.usuario import Usuario
from db.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Response_usuario)
def crear_usuario(usuario: schemas.Crear_usuario, db: Session = Depends(get_db)):
  nuevo_usuario = Usuario(
    nombre_usuario = usuario.nombre_usuario,
    rol_usuario = usuario.rol_usuario,
    contrasenia_usuario = usuario.contrasenia_usuario
  )
  db.add(nuevo_usuario)
  db.commit()
  db.refresh(nuevo_usuario) # La variable no sabe el id asignado, con refresh SQLAlchemy mira la bd y lee el id nuevo y se lo inyecta a la variable
  return nuevo_usuario
