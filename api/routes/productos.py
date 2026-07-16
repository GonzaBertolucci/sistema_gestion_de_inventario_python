from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional


from crud import crud_productos
from db.database import get_db
from schemas.producto import (
    Agregar_Producto,
    Modificar_Producto,
    Borrar_Producto,
    Response_Producto,
)

router = APIRouter()


@router.post("/add", response_model=Response_Producto)
def agregar_producto(producto: Agregar_Producto, db: Session = Depends(get_db)):

    nuevo_producto = crud_productos.agregar_nuevo_producto(
        db=db, producto_data=producto
    )

    return nuevo_producto


@router.get("/lista", response_model=List[Response_Producto])
def mostrar_productos(
    db: Session = Depends(get_db),
    id_Prov: Optional[int] = None,
    id_Cat: Optional[int] = None,
    nombre: Optional[str] = None,
    stock_min: Optional[int] = None,
    stock_max: Optional[int] = None,
    precio_venta_min: Optional[float] = None,
    precio_venta_max: Optional[float] = None,
    coste_min: Optional[float] = None,
    coste_max: Optional[float] = None,
    cod_barra: Optional[str] = None,
):
    producto = crud_productos.leer_productos(
        db,
        nombre=nombre,
        id_Prov=id_Prov,
        id_Cat=id_Cat,
        stock_min=stock_min,
        stock_max=stock_max,
        precio_venta_max=precio_venta_max,
        precio_venta_min=precio_venta_min,
        coste_min=coste_min,
        coste_max=coste_max,
        cod_barra=cod_barra,
    )
    return producto


@router.put("/mod", response_model=Response_Producto)
def modificar_proveedor(
    producto_data: Modificar_Producto, db: Session = Depends(get_db)
):
    producto_actualizado = crud_productos.actualizar_productos(
        db=db, id_Prod=producto_data.id_Prod, producto_data=producto_data
    )

    if not producto_actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto_actualizado


@router.put("/borrar", response_model=Response_Producto)
def borrar_producto(producto_data: Borrar_Producto, db: Session = Depends(get_db)):
    producto_por_borrar = crud_productos.dar_de_baja_productos(
        db=db, id_Prod=producto_data.id_Prod
    )

    if not producto_por_borrar:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto_por_borrar
