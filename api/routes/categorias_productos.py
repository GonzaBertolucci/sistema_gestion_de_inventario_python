from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.categoria_producto import Agregar_Categoria_Producto , Response_Categoria_Producto
from crud.crud_categoria_producto import AgregarCategoriaProducto

router = APIRouter()


@router.post("/", response_model=Response_Categoria_Producto)
def agregar_cat(cat: Agregar_Categoria_Producto, db: Session = Depends(get_db)):

    nueva_cat = AgregarCategoriaProducto(db=db, cat_prod_data=cat)

    return nueva_cat
