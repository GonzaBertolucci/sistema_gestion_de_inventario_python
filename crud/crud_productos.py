from sqlalchemy.orm import Session
from models.producto import Producto
from schemas.producto import Agregar_Producto

# C R U D temporal productos


def Agregar_nuevo_producto(db: Session, producto_data: Agregar_Producto):
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
