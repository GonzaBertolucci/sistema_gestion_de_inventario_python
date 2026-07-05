from typing import Optional

from sqlalchemy.orm import Session
from models.proveedor import Proveedor
from schemas.proveedor import Agregar_Proveedor

# C R U D proveedores


def agregar_nuevo_proveedor(db: Session, provedor_data: Agregar_Proveedor):
    nuevo_proveedor = Proveedor(nombre_Prov=provedor_data.nombre_Prov)

    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)

    return nuevo_proveedor


def Leer_provs(db: Session, nombre: Optional[str] = None):
    query = db.query(Proveedor).filter(Proveedor.prov_Activo == True)

    if nombre:
        query = query.filter(Proveedor.nombre_Prov.ilike(f"%{nombre}%"))

    return query.all()


"""
class updateProveedor:
    print("Proveedor modificado correctamente")


class deleteProveedor:
    #Aca va el modificar
    print("Se elimino el Proveedor correctamente")
"""
