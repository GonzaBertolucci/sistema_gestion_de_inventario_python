from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship


from db.database import Base

class Usuario(Base):
  __tablename__ = 'usuarios'
  id_usuario = Column(Integer, primary_key=True, autoincrement=True)
  nombre_usuario = Column(String(50), nullable=False, unique=True)
  contrasenia_usuario = Column(String(300), nullable=False)
  rol_usuario = Column(Boolean, nullable=False)
  activo = Column(Boolean, default=True)
  ventas = relationship("Ventas", back_populates="vendedor")
