from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Detalles_de_ventas(Base):
  __tablename__ = 'detalles_de_ventas'
  id_detalle = Column(Integer, primary_key=True)
  id_venta = Column(Integer, ForeignKey('ventas.id_venta'))
  id_producto = Column(Integer, ForeignKey('productos.id_Prod'), nullable=False)
  cantidad = Column(Integer, nullable=False)
  precio_x_unidad = Column(Float, nullable=False)
  venta = relationship("Ventas", back_populates="detalles")