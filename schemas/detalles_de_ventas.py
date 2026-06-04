from pydantic import BaseModel

class Crear_detalle_venta(BaseModel):
  id_producto: int
  cantidad: int
  precio_x_unidad: float
  
class Response_detalle_venta(BaseModel):
  id_detalle: int
  id_venta: int
  id_producto: int
  cantidad: int
  precio_x_unidad: float
  class Config:
    from_attributes = True