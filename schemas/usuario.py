from typing import Optional

from pydantic import BaseModel

# Molde para internet (FastAPI), usa tipo nativos de python y valida los datos JSON que entran y salen por la web
class UsuarioBase(BaseModel):
    nombre_usuario: str
    rol_usuario: bool
    activo: Optional[bool] = True

#Molde POST (Hereda de arriba y suma la contraseña)
class UsuarioCreate(UsuarioBase):
    contrasenia_usuario: str
    
#Molde PUT
class UsuarioUpdate(BaseModel):
    nombre_usuario: Optional[str] = None
    rol_usuario: Optional[bool] = None
    contrasenia_usuario: Optional[str] = None
    activo: Optional[bool] = True

class Response_usuario(UsuarioBase):
    id_usuario: int
    
    class Config:
        from_attributes = True
