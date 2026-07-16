from pydantic import BaseModel
from typing import Optional


class Agregar_Producto(BaseModel):
    id_Prov: int
    id_Cat: int
    nombre_Prod: str
    desc_Prod: str
    precio_Cost_Prod: float
    precio_Venta_Prod: float
    stock_Prod: int
    cod_Barrs_Prod: str


class Modificar_Producto(BaseModel):
    id_Prod: int
    id_Prov: Optional[int] = None
    id_Cat: Optional[int] = None
    nombre_Prod: Optional[str] = None
    desc_Prod: Optional[str] = None
    precio_Cost_Prod: Optional[float] = None
    precio_Venta_Prod: Optional[float] = None
    stock_Prod: Optional[int] = None
    cod_Barrs_Prod: Optional[str] = None


class Borrar_Producto(BaseModel):
    id_Prod: int


class Response_Producto(BaseModel):
    id_Prod: int
    id_Prov: int
    id_Cat: int
    nombre_Prod: str
    desc_Prod: str
    precio_Cost_Prod: float
    precio_Venta_Prod: float
    stock_Prod: int
    cod_Barrs_Prod: str
    prod_Activo: bool

    class Config:
        from_attributes = True
