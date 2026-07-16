from pydantic import BaseModel
from typing import Optional


class Agregar_Proveedor(BaseModel):
    nombre_Prov: str


class Modificar_Proveedor(BaseModel):
    id_Prov: int
    nombre_Prov: Optional[str] = None


class Borrar_Proveedor(BaseModel):
    id_Prov: int


class Response_Proovedor(BaseModel):
    id_Prov: int
    nombre_Prov: str
    prov_Activo: bool

    class Config:
        from_attributes = True
