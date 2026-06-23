from sqlalchemy.orm import Session
from models.categoria_producto import Cat_Prod
from schemas.categoria_producto import Agregar_Categoria_Producto

# C R U D categoria de productos


def AgregarCategoriaProducto(db: Session, cat_prod_data: Agregar_Categoria_Producto):
    nueva_categoria = Cat_Prod(
        nombre_Cat=cat_prod_data.nombre_Cat, desc_Cat=cat_prod_data.desc_Cat
    )

    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)

    return nueva_categoria
