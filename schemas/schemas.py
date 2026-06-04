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
