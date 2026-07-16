from typing import Optional

from sqlalchemy.orm import Session
from models.producto import Producto
from schemas.producto import Agregar_Producto, Modificar_Producto


def agregar_nuevo_producto(db: Session, producto_data: Agregar_Producto):
    nuevo_producto = Producto(
        id_Prov=producto_data.id_Prov,
        id_Cat=producto_data.id_Cat,
        nombre_Prod=producto_data.nombre_Prod,
        desc_Prod=producto_data.desc_Prod,
        precio_Cost_Prod=producto_data.precio_Cost_Prod,
        precio_Venta_Prod=producto_data.precio_Venta_Prod,
        stock_Prod=producto_data.stock_Prod,
        cod_Barrs_Prod=producto_data.cod_Barrs_Prod,
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


def Agregar_nuevo_producto2(db: Session, producto_data: Agregar_Producto):
    nuevo_producto = Producto(**producto_data.model_dump())

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto


def Leer_productos(
    db: Session,
    id_Prod: Optional[int] = None,
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
    query = db.query(Producto).filter(Producto.prod_Activo == True)

    if id_Prod:
        query = query.filter(Producto.id_Prod == id_Prod)

    if id_Prov:
        query = query.filter(Producto.id_Prov == id_Prov)

    if id_Cat:
        query = query.filter(Producto.id_Cat == id_Cat)

    if nombre:
        query = query.filter(Producto.nombre_Prod.ilike(f"%{nombre}%"))

    if stock_min:
        query = query.filter(Producto.stock_Prod >= stock_min)

    if stock_max:
        query = query.filter(Producto.stock_Prod <= stock_max)

    if precio_venta_min:
        query = query.filter(Producto.precio_Venta_Prod >= precio_venta_min)

    if precio_venta_max:
        query = query.filter(Producto.precio_Venta_Prod <= precio_venta_max)

    if coste_min:
        query = query.filter(Producto.precio_Cost_Prod >= coste_min)

    if coste_max:
        query = query.filter(Producto.precio_Cost_Prod <= coste_max)

    if cod_barra:
        query = query.filter(Producto.cod_Barrs_Prod.ilike(f"%{cod_barra}%"))

    return query.all()


def actualizar_productos(
    db: Session,
    id_Prod: int,
    producto_data: Modificar_Producto,
):

    Producto_bd = db.query(Producto).filter(Producto.id_Prod == id_Prod).first()

    if not Producto_bd:
        return None

    update_data = producto_data.model_dump(exclude_unset=True)

    update_data.pop("id_Prod", None)

    for key, value in update_data.items():
        setattr(Producto_bd, key, value)

    db.commit()
    db.refresh(Producto_bd)

    return Producto_bd


def dar_de_baja_productos(db: Session, id_Prod: int):
    producto_data = db.query(Producto).filter(Producto.id_Prod == id_Prod).first()

    if not producto_data:
        return None

    producto_data.prod_Activo = False

    db.commit()
    db.refresh(producto_data)

    return producto_data
