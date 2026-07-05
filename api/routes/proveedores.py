from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from db.database import get_db
from schemas.proveedor import Agregar_Proveedor, Response_Proovedor
from crud.crud_proveedores import agregar_nuevo_proveedor, Leer_provs

router = APIRouter()


@router.post("/add", response_model=Response_Proovedor)
def agregar_proveedor(proveedor: Agregar_Proveedor, db: Session = Depends(get_db)):

    nuevo_proveedor = agregar_nuevo_proveedor(db=db, provedor_data=proveedor)

    return nuevo_proveedor


@router.post("/lista", response_model=List[Response_Proovedor])
def Mostrar_proveedores(nombre: Optional[str] = None, db: Session = Depends(get_db)):
    proveedores = Leer_provs(db, nombre=nombre)
    return proveedores
