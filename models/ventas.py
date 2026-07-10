from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from db.database import Base


class Ventas(Base):
  __tablename__ = 'ventas'
  id_venta = Column(Integer, primary_key=True, autoincrement=True)
  fecha_hora = Column(DateTime(), default=datetime.now)
  id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'))
  total = Column(Float, nullable=False)
  metodo_de_pago = Column(String(50))
  activo = Column(Boolean, default=True)
  vendedor = relationship("Usuario", back_populates="ventas")
  detalles = relationship("Detalles_de_ventas", back_populates="venta")
  
  #Refactor usuario schemas and CRUD operations to use updated data models; add new product creation function in CRUD.