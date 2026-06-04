from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import Crear_usuario

def crear_nuevo_usuario(db: Session, usuario_data: Crear_usuario):
    nuevo_usuario = Usuario(
        nombre_usuario = usuario_data.nombre_usuario,
        rol_usuario = usuario_data.rol_usuario,
        contrasenia_usuario = usuario_data.contrasenia_usuario
    )
    
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return nuevo_usuario