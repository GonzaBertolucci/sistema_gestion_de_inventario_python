from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Proveedor(Base):
    __tablename__ = "proveedores"
    id_Prov = Column(Integer(), primary_key=True, autoincrement=True)
    nombre_Prov = Column(String(50), nullable=False, unique=True)
    prov_Activo = Column(Boolean, default=True, nullable=False)
    proveedor = relationship("Producto", back_populates="provEnProd")
