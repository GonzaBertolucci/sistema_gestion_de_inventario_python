from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional


from crud import crud_proveedores
from db.database import get_db
from schemas.proveedor import (
    Agregar_Proveedor,
    Modificar_Proveedor,
    Borrar_Proveedor,
    Response_Proovedor,
)

router = APIRouter()


@router.post("/add", response_model=Response_Proovedor)
def agregar_proveedor(proveedor: Agregar_Proveedor, db: Session = Depends(get_db)):

    nuevo_proveedor = crud_proveedores.agregar_nuevo_proveedor(
        db=db, provedor_data=proveedor
    )

    return nuevo_proveedor


@router.post("/lista", response_model=List[Response_Proovedor])
def mostrar_proveedores(
    db: Session = Depends(get_db),
    id_Prov: Optional[int] = None,
    nombre: Optional[str] = None,
):
    proveedores = crud_proveedores.leer_proveedores(db, id_Prov=id_Prov, nombre=nombre)
    return proveedores


@router.get("/mod", response_model=Response_Proovedor)
def modificar_proveedor(
    proveedor_data: Modificar_Proveedor, db: Session = Depends(get_db)
):
    proveedor_actualizado = crud_proveedores.actualizar_proveedores(
        db=db, id_Prov=proveedor_data.id_Prov, proveedor_data=proveedor_data
    )

    if not proveedor_actualizado:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")

    return proveedor_actualizado


@router.put("/borrar", response_model=Response_Proovedor)
def borrar_proveedor(proveedor_data: Borrar_Proveedor, db: Session = Depends(get_db)):
    proveedor_por_borrar = crud_proveedores.dar_de_baja_proveedores(
        db=db, id_Prov=proveedor_data.id_Prov
    )

    if not proveedor_por_borrar:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")

    return proveedor_por_borrar
