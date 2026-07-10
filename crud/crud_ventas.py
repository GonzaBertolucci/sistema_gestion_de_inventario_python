from sqlalchemy.orm import Session
from models.ventas import Ventas
from models.detalles_de_ventas import Detalles_de_ventas
from schemas.ventas import VentasCreate, VentasUpdate
from models.producto import Producto

def crear_nueva_venta(db: Session, venta_data: VentasCreate):
  
  total_calculado = 0
  
  for detalle in venta_data.detalles:
    producto_db = db.query(Producto).filter(Producto.id_Prod == detalle.id_producto).first()
    
    if producto_db is None:
      raise ValueError(f"El producto con ID {detalle.id_producto} no existe.")
    
    total_calculado += detalle.cantidad * producto_db.precio_Venta_Prod
    
  nueva_venta = Ventas(
    id_usuario = venta_data.id_usuario,
    total = total_calculado,
    metodo_de_pago = venta_data.metodo_de_pago
  )
  
  db.add(nueva_venta)
  db.commit()
  db.refresh(nueva_venta)
  
  for detalle in venta_data.detalles:
    producto_db = db.query(Producto).filter(Producto.id_Prod == detalle.id_producto).first()
    
    nuevo_detalle = Detalles_de_ventas(
      id_venta = nueva_venta.id_venta,
      id_producto = detalle.id_producto,
      cantidad = detalle.cantidad,
      precio_x_unidad = producto_db.precio_Venta_Prod
    )
    db.add(nuevo_detalle)
  
  db.commit()
  db.refresh(nueva_venta)
  
  return nueva_venta

def obtener_todas_las_ventas(db: Session):
  return db.query(Ventas).all()

def obtener_venta_por_id(db: Session, venta_id: int):
  return db.query(Ventas).filter(Ventas.id_venta == venta_id).first()

def eliminar_venta(db: Session, venta_id: int):
  venta_db = obtener_venta_por_id(db, venta_id)
  
  if venta_db is None:
    return None
  
  venta_db.activo = False
  
  db.commit()
  db.refresh(venta_db)
  
  return venta_db

def actualizar_venta(db: Session, venta_id: int, venta_actualizada: VentasUpdate):
  venta_db = obtener_venta_por_id(db, venta_id)
  
  if venta_db is None:
    return None
  
  if venta_actualizada.metodo_de_pago is not None:
    venta_db.metodo_de_pago = venta_actualizada.metodo_de_pago
    
  db.commit()
  db.refresh(venta_db)
    
  return venta_db
