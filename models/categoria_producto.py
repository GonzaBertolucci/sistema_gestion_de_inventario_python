from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Cat_Prod(Base):
    __tablename__ = "catsDeProducto"
    id_Cat = Column(Integer(), primary_key=True, autoincrement=True)
    nombre_Cat = Column(String(50), nullable=False)
    desc_Cat = Column(String(50), nullable=False)
    cat_Activo = Column(Boolean, default=True, nullable=False)
    categoria = relationship("Producto", back_populates="catEnProd")
