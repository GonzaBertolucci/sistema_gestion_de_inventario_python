from pydantic import BaseModel
from datetime import datetime
from typing import List
from schemas.detalles_de_ventas import Crear_detalle_venta, Response_detalle_venta

class Crear_venta(BaseModel):
    id_usuario: int
    total: float
    metodo_de_pago: str
    detalles: List[Crear_detalle_venta]


class Response_venta(BaseModel):
    id_venta: int
    fecha_hora: datetime
    id_usuario: int
    total: float
    metodo_de_pago: str
    activo: bool
    detalles: List[Response_detalle_venta]

    class Config:
        from_attributes = True
