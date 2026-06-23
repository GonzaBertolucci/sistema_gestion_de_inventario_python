from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.producto import Agregar_Producto, Response_Producto
from crud.crud_productos import Agregar_nuevo_producto

router = APIRouter()


@router.post("/", response_model=Response_Producto)
def Agregar_producto(producto: Agregar_Producto, db: Session = Depends(get_db)):

    nuevo_producto = Agregar_nuevo_producto(db=db, producto_data=producto)

    return nuevo_producto
