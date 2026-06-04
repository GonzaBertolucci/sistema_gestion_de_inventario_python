from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime

from db.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(50), nullable=False, unique=True)
    contrasenia_usuario = Column(String(300), nullable=False)
    rol_usuario = Column(Boolean, nullable=False)
    activo = Column(Boolean, default=True)
    ventas = relationship("Ventas", back_populates="vendedor")


class Ventas(Base):
    __tablename__ = "ventas"
    id_venta = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime(), default=datetime.now)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    total = Column(Float, nullable=False)
    metodo_de_pago = Column(String(50))
    activo = Column(Boolean, default=True)
    vendedor = relationship("Usuario", back_populates="ventas")
    detalles = relationship("Detalles_de_ventas", back_populates="venta")
