from typing import Optional

from sqlalchemy.orm import Session
from models.categoria_producto import Cat_Prod
from schemas.categoria_producto import (
    Agregar_Categoria_Producto,
    Modificar_Categoria_Producto,
)


def agregar_nueva_categoria_producto(
    db: Session, cat_prod_data: Agregar_Categoria_Producto
):
    nueva_categoria = Cat_Prod(
        nombre_Cat=cat_prod_data.nombre_Cat, desc_Cat=cat_prod_data.desc_Cat
    )

    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)

    return nueva_categoria


def leer_categoria_producto(db: Session, nombre: Optional[str] = None):
    query = db.query(Cat_Prod).filter(Cat_Prod.cat_Activo == True)

    if nombre:
        query = query.filter(Cat_Prod.nombre_Cat.ilike(f"%{nombre}%"))

    return query.all()


def actualizar_categoria_producto(
    db: Session, id_Cat: int, cat_prod_data: Modificar_Categoria_Producto
):

    categoria_bd = db.query(Cat_Prod).filter(Cat_Prod.id_Cat == id_Cat).first()

    if not categoria_bd:
        return None

    update_data = cat_prod_data.model_dump(exclude_unset=True)

    update_data.pop("id_Cat", None)

    for key, value in update_data.items():
        setattr(categoria_bd, key, value)

    db.commit()
    db.refresh(categoria_bd)

    return categoria_bd


def dar_de_baja_categoria_producto(
    db: Session,
    id_Cat: int,
):

    categoria_bd = db.query(Cat_Prod).filter(Cat_Prod.id_Cat == id_Cat).first()

    if not categoria_bd:
        return None

    categoria_bd.cat_Activo = False

    db.commit()
    db.refresh(categoria_bd)

    return categoria_bd
