from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from schemas.detalles_de_ventas import Crear_detalle_venta, Response_detalle_venta

class VentasBase(BaseModel):
    metodo_de_pago: str
    activo: bool

class VentasCreate(VentasBase):
    id_usuario: int
    detalles: List[Crear_detalle_venta]
    
class VentasUpdate(BaseModel):
    id_usuario: Optional[int] = None
    total: Optional[float] = None
    metodo_de_pago: Optional[str] = None
    activo: Optional[bool] = None
    detalles: Optional[List[Crear_detalle_venta]] = None

class Response_venta(VentasBase):
    id_venta: int
    fecha_hora: datetime
    id_usuario: int
    total: float
    detalles: List[Response_detalle_venta]
    
    class Config:
        from_attributes = True
