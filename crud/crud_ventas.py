from sqlalchemy.orm import Session
from models.ventas import Ventas
from models.detalles_de_ventas import Detalles_de_ventas
from schemas.ventas import Crear_venta

def crear_nueva_venta(db: Session, venta_data: Crear_venta):
  nueva_venta = Ventas(
    id_usuario = venta_data.id_usuario,
    total = venta_data.total,
    metodo_de_pago = venta_data.metodo_de_pago
  )
  
  db.add(nueva_venta)
  db.commit()
  db.refresh(nueva_venta)
  
  for detalle in venta_data.detalles:
    nuevo_detalle = Detalles_de_ventas(
      id_venta = nueva_venta.id_venta,
      id_producto = detalle.id_producto,
      cantidad = detalle.cantidad,
      precio_x_unidad = detalle.precio_x_unidad
    )
    db.add(nuevo_detalle)
  
  db.commit()
  db.refresh(nueva_venta)
  
  return nueva_venta