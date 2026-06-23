from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.usuario import Crear_usuario, Response_usuario
from crud.crud_usuarios import crear_nuevo_usuario

router = APIRouter()

@router.post("/", response_model=Response_usuario)
def crear_usuario(usuario: Crear_usuario, db: Session = Depends(get_db)):
    
    nuevo_usuario = crear_nuevo_usuario(db=db, usuario_data=usuario)
    
    return nuevo_usuario
