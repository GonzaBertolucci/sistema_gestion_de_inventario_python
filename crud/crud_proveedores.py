from typing import Optional

from sqlalchemy.orm import Session
from models.proveedor import Proveedor
from schemas.proveedor import Agregar_Proveedor, Modificar_Proveedor

# C R U D proveedores
# funciones = snake_case
# Classes CamelCase


def agregar_nuevo_proveedor(db: Session, provedor_data: Agregar_Proveedor):
    nuevo_proveedor = Proveedor(nombre_Prov=provedor_data.nombre_Prov)

    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)

    return nuevo_proveedor


def leer_proveedores(
    db: Session, id_Prov: Optional[int] = None, nombre: Optional[str] = None
):
    query = db.query(Proveedor).filter(Proveedor.prov_Activo == True)

    if id_Prov:
        query = query.filter(Proveedor.id_Prov == id_Prov)

    if nombre:
        query = query.filter(Proveedor.nombre_Prov.ilike(f"%{nombre}%"))

    return query.all()


def actualizar_proveedores(
    db: Session, id_Prov: int, proveedor_data: Modificar_Proveedor
):

    proveedor_bd = db.query(Proveedor).filter(Proveedor.id_Prov == id_Prov).first()

    if not proveedor_bd:
        return None

    update_data = proveedor_data.model_dump(exclude_unset=True)

    update_data.pop("id_Prov", None)

    for key, value in update_data.items():
        setattr(proveedor_bd, key, value)

    db.commit()
    db.refresh(proveedor_bd)

    return proveedor_bd


def dar_de_baja_proveedores(
    db: Session,
    id_Prov: int,
):

    proveedor_bd = db.query(Proveedor).filter(Proveedor.id_Prov == id_Prov).first()

    if not proveedor_bd:
        return None

    proveedor_bd.prov_Activo = False

    db.commit()
    db.refresh(proveedor_bd)

    return proveedor_bd
