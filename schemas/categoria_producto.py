from pydantic import BaseModel
from typing import Optional


class Agregar_Categoria_Producto(BaseModel):
    nombre_Cat: str
    desc_Cat: str


class Modificar_Categoria_Producto(BaseModel):
    id_Cat: int
    nombre_Cat: Optional[str] = None
    desc_Cat: Optional[str] = None


class Borrar_Categoria_Producto(BaseModel):
    id_Cat: int


class Response_Categoria_Producto(BaseModel):
    id_Cat: int
    nombre_Cat: str
    desc_Cat: str
    cat_Activo: bool

    class Config:
        from_attributes = True
