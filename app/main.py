from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models.models as models
import schemas.schemas as schemas

from db.database import Base, engine, SessionLocal

Base.metadata.create_all(bind = engine)

app = FastAPI(title="Gestión de Inventario")

'''
# Incluyes las rutas separadas
app.include_router(proveedores.router, prefix="/proveedores", tags=["Proveedores"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
'''

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