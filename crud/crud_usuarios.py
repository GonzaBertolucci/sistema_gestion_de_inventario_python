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