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

#Trae todos los usuarios, el .all() le dice a Alchemy que traiga todo
def obtener_todos_los_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    ## .filter() es el where de SQL, y .first() devuelve el primer resultado de la consulta
    return db.query(Usuario).filter(Usuario.id_usuario == usuario_id).first()

def actualizar_usuario(db: Session, usuario_id: int, datos_actualizados: Crear_usuario):
    usuario_db=obtener_usuario_por_id (db, usuario_id)
    
    if usuario_db is None:
        return None
    
    usuario_db.nombre_usuario = datos_actualizados.nombre_usuario
    usuario_db.rol_usuario = datos_actualizados.rol_usuario
    usuario_db.contrasenia_usuario = datos_actualizados.contrasenia_usuario
    
    db.commit()
    db.refresh(usuario_db)
    
    return usuario_db

def eliminar_usuario_logico(db: Session, usuario_id: int):
    usuario_db = obtener_usuario_por_id(db, usuario_id)
    
    if usuario_db is None:
        return None
    
    usuario_db.activo = False
    
    db.commit()
    db.refresh(usuario_db)
    
    return usuario_db