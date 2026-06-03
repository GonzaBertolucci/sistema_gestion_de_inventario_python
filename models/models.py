from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime

from db.database import Base

class Usuario(Base):
  __tablename__ = 'usuarios'
  id_usuario = Column(Integer, primary_key=True, autoincrement=True)
  nombre_usuario = Column(String(50), nullable=False, unique=True)
  contrasenia_usuario = Column(String(300), nullable=False)
  rol_usuario = Column(Boolean, nullable=False)
  activo = Column(Boolean, default=True)
  ventas = relationship("Ventas", back_populates="vendedor")

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
 
class Detalles_de_ventas(Base):
  __tablename__ = 'detalles_de_ventas'
  id_detalle = Column(Integer, primary_key=True)
  id_venta = Column(Integer, ForeignKey('ventas.id_venta'))
  id_producto = Column(Integer, ForeignKey('productos.id_Prod'), nullable=False)
  cantidad = Column(Integer, nullable=False)
  precio_x_unidad = Column(Float, nullable=False)
  venta = relationship("Ventas", back_populates="detalles")

class Proveedor(Base):
    __tablename__ = "proveedores"
    id_Prov = Column (Integer(), primary_key=True, autoincrement=True)
    nombre_Prov = Column (String(50), nullable = False, unique=True)
    prov_Activo = Column (Boolean, default=True, nullable = False)
    proveedor = relationship("Producto",back_populates="provEnProd")

class Cat_Prod(Base):
    __tablename__ = "catsDeProducto"
    id_Cat = Column (Integer(), primary_key=True, autoincrement=True)
    nombre_Cat = Column (String(50), nullable = False)
    desc_Cat = Column (String(50), nullable = False)
    cat_Activo = Column (Boolean, default=True, nullable = False)
    categoria = relationship("Producto",back_populates="catEnProd")

class Producto(Base):
    __tablename__ = "productos"
    id_Prod = Column (Integer(), primary_key=True, autoincrement=True)
    id_Prov = Column (Integer(), ForeignKey("proveedores.id_Prov") )
    id_Cat = Column (Integer(), ForeignKey("catsDeProducto.id_Cat"))
    nombre_Prod = Column (String(50), nullable = False)
    desc_Prod = Column (String(50), nullable = False)
    precio_Cost_Prod = Column (Float())
    precio_Venta_Prod = Column (Float())
    stock_Prod = Column (Integer())
    cod_Barrs_Prod = Column (Integer())
    prod_Activo = Column (Boolean, default=True, nullable = False)
    provEnProd = relationship("Proveedor",back_populates="proveedor")
    catEnProd = relationship("Cat_Prod",back_populates="categoria")