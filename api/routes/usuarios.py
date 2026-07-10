from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.usuario import UsuarioCreate, Response_usuario, UsuarioBase, UsuarioUpdate
from crud.crud_usuarios import crear_nuevo_usuario, obtener_todos_los_usuarios,obtener_usuario_por_id, actualizar_usuario, eliminar_usuario_logico
from typing import List


router = APIRouter()
#C = Create - POST
@router.post("/", response_model=Response_usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    
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

#U = Update - PUT
@router.put("/{usuario_id}", response_model=Response_usuario)
def modificar_usuario(usuario_id: int, datos_nuevos: UsuarioUpdate,db: Session = Depends(get_db)):
    
    usuario_actualizado = actualizar_usuario(db=db, usuario_id = usuario_id, datos_actualizados = datos_nuevos)
    
    if usuario_actualizado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "El usuario a modificar no existe")

    return usuario_actualizado

#D = Delete - DELETE
@router.delete("/{usuario_id}", response_model= Response_usuario)
def borrar_usuario(usuario_id: int, db:Session = Depends(get_db)):
    usuario_eliminado = eliminar_usuario_logico(db=db, usuario_id=usuario_id)
    
    if usuario_eliminado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "El usuario a eliminar no existe")
    
    return usuario_eliminado