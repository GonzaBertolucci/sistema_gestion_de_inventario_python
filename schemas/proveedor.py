from pydantic import BaseModel


class Agregar_Proveedor(BaseModel):
    nombre_Prov: str


class Response_Proovedor(BaseModel):
    id_Prov: int
    nombre_Prov: str
    prov_Activo: bool

    class Config:
        from_attributes = True
