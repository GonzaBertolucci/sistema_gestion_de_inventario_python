from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.ventas import Crear_venta, Response_venta
from crud.crud_ventas import crear_nueva_venta

router = APIRouter()

@router.post("/", response_model=Response_venta)
def registrar_venta(venta: Crear_venta, db: Session = Depends(get_db)):
  
    nueva_venta = crear_nueva_venta(db=db, venta_data=venta)
    
    return nueva_venta