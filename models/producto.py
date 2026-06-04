from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base

class Producto(Base):
    __tablename__ = "productos"
    id_Prod = Column(Integer(), primary_key=True, autoincrement=True)
    id_Prov = Column(Integer(), ForeignKey("proveedores.id_Prov"))
    id_Cat = Column(Integer(), ForeignKey("catsDeProducto.id_Cat"))
    nombre_Prod = Column(String(50), nullable=False)
    desc_Prod = Column(String(50), nullable=False)
    precio_Cost_Prod = Column(Float())
    precio_Venta_Prod = Column(Float())
    stock_Prod = Column(Integer())
    cod_Barrs_Prod = Column(Integer())
    prod_Activo = Column(Boolean, default=True, nullable=False)
    provEnProd = relationship("Proveedor", back_populates="proveedor")
    catEnProd = relationship("Cat_Prod", back_populates="categoria")
