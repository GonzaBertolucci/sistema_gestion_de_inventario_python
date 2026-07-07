from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.usuario import Crear_usuario, Response_usuario
from crud.crud_usuarios import crear_nuevo_usuario, obtener_todos_los_usuarios,obtener_usuario_por_id
from typing import List


router = APIRouter()
#C = Create - POST
@router.post("/", response_model=Response_usuario)
def crear_usuario(usuario: Crear_usuario, db: Session = Depends(get_db)):
    
    nuevo_usuario = crear_nuevo_usuario(db=db, usuario_data=usuario)
    
    return nuevo_usuario
#R = Read - GET
@router.get("/", response_model=List[Response_usuario])
def leer_usuarios(db: Session = Depends(get_db)):
    lista_de_usuarios = obtener_todos_los_usuarios(db=db)
    
    return lista_de_usuarios

@router.get("/{usuario_id}", response_model=Response_usuario)
def leer_usuario_por_id(usuario_id: int, db:Session = Depends(get_db)):
    usuario = obtener_usuario_por_id(db=db, usuario_id=usuario_id)
    
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Usuario no encontrado")

    return usuario
