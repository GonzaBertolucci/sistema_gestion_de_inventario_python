from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from crud import crud_categoria_producto
from db.database import get_db
from schemas.categoria_producto import (
    Agregar_Categoria_Producto,
    Response_Categoria_Producto,
    Modificar_Categoria_Producto,
    Borrar_Categoria_Producto,
)

router = APIRouter()


@router.post("/add", response_model=Response_Categoria_Producto)
def agregar_categoria_producto(
    cat: Agregar_Categoria_Producto, db: Session = Depends(get_db)
):

    nueva_cat = crud_categoria_producto.agregar_nueva_categoria_producto(
        db=db, cat_prod_data=cat
    )

    return nueva_cat


@router.get("/lista", response_model=List[Response_Categoria_Producto])
def mostrar_categoria_producto(
    nombre: Optional[str] = None, db: Session = Depends(get_db)
):
    cat = crud_categoria_producto.leer_categoria_producto(db, nombre=nombre)
    return cat


@router.put("/mod", response_model=Response_Categoria_Producto)
def modificar_categoria(
    cat_prod_data: Modificar_Categoria_Producto, db: Session = Depends(get_db)
):
    categoria_a_actualizar = crud_categoria_producto.actualizar_categoria_producto(
        db=db, id_Cat=cat_prod_data.id_Cat, cat_prod_data=cat_prod_data
    )

    if not categoria_a_actualizar:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")

    return categoria_a_actualizar


@router.put("/borrar", response_model=Response_Categoria_Producto)
def borrar_categoria_producto(
    cat_data: Borrar_Categoria_Producto, db: Session = Depends(get_db)
):
    categoria_a_borrar = crud_categoria_producto.dar_de_baja_categoria_producto(
        db=db, id_Cat=cat_data.id_Cat
    )

    if not categoria_a_borrar:
        raise HTTPException(status_code=404, detail="Categoria no encontrado")

    return categoria_a_borrar
