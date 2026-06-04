from pydantic import BaseModel


class Agregar_Producto(BaseModel):
    nombre_Prod = str
    desc_Prod = str
    precio_Cost_Prod = float
    precio_Venta_Prod = float
    stock_Prod = int
    cod_Barrs_Prod = int


class Response_Producto(BaseModel):
    id_Prod = int
    id_Prov = int
    id_Cat = int
    nombre_Prod = str
    desc_Prod = str
    precio_Cost_Prod = float
    precio_Venta_Prod = float
    stock_Prod = int
    cod_Barrs_Prod = int
    prod_Activo = bool

    class Config:
        from_attributes = True
