from fastapi import FastAPI, Depends
from sqlalchemy import String, select
from sqlalchemy.orm import Session

from db.database import SessionLocal
import models.producto as models
import schemas.producto as schemas

# C R U D temporal productos

app = FastAPI()
db = SessionLocal()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/productos/", response_model=schemas.Response_Producto)
def Agregar_producto(producto: schemas.Agregar_Producto, db: Session = Depends(get_db)):
    nuevo_producto = models.Producto(
        nombre_Prod=producto.nombre_Prod,
        desc_Prod=producto.desc_Prod,
        precio_Cost_Prod=producto.precio_Cost_Prod,
        precio_Venta_Prod=producto.precio_Venta_Prod,
        stock_Prod=producto.stock_Prod,
        cod_Barrs_Prod=producto.cod_Barrs_Prod,
    )

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto
