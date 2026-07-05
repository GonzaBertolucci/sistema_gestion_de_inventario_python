from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.producto import Agregar_Producto, Response_Producto
from crud.crud_productos import Agregar_nuevo_producto, Leer_productos

router = APIRouter()


@router.post("/add", response_model=Response_Producto)
def Agregar_producto(producto: Agregar_Producto, db: Session = Depends(get_db)):

    nuevo_producto = Agregar_nuevo_producto(db=db, producto_data=producto)

    return nuevo_producto


@router.post("/lista", response_model=List[Response_Producto])
def Mostrar_productos(
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
    producto = Leer_productos(
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
