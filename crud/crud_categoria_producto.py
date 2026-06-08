from fastapi import FastAPI, Depends
from sqlalchemy import String, select
from sqlalchemy.orm import Session

from db.database import SessionLocal
import models.categoria_producto as models
import schemas.categoria_producto as schemas

# C R U D categoria de productos

app = FastAPI()
db = SessionLocal()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/c/", response_model=schemas.Response_Categoria_Producto)
def AgregarCategoriaProducto(
    cat_prod: schemas.Response_Categoria_Producto, db: Session = Depends(get_db)
):
    nueva_categoria = models.Cat_Prod(
        nombre_Cat=cat_prod.nombre_Cat,
        desc_Cat=cat_prod.desc_Cat
    )
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria
