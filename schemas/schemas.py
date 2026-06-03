from pydantic import BaseModel
# Molde para internet (FastAPI), usa tipo nativos de python y valida los datos JSON que entran y salen por la web
class Crear_usuario(BaseModel):
  nombre_usuario: str
  contrasenia_usuario: str
  rol_usuario: bool
  
class Response_usuario(BaseModel):
  id_usuario: int
  nombre_usuario: str
  rol_usuario: bool
  activo: bool
  class Config:
    from_attributes = True

class Agregar_Proveedor(BaseModel):
  nombre_Prov : str

class Response_Proovedor(BaseModel):
  id_Prov : int
  nombre_Prov : str
  prov_Activo : bool
  class Config:
    from_attributes = True