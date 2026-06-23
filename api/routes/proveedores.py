from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.proveedor import Agregar_Proveedor, Response_Proovedor
from crud.crud_proveedores import agregar_nuevo_proveedor

router = APIRouter()


@router.post("/", response_model=Response_Proovedor)
def agregar_proveedor(proveedor: Agregar_Proveedor, db: Session = Depends(get_db)):

    nuevo_proveedor = agregar_nuevo_proveedor(db=db, provedor_data=proveedor)

    return nuevo_proveedor
