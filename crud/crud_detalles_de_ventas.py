from sqlalchemy.orm import Session
from models.detalles_de_ventas import Detalles_de_ventas

def obtener_detalles_por_venta(db: Session, venta_id: int):
  return db.query(Detalles_de_ventas).filter(Detalles_de_ventas.id_venta == venta_id).all()
