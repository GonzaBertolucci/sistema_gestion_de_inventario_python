from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.ventas import Response_detalle_venta 
from crud.crud_detalles_de_ventas import obtener_detalles_por_venta

router = APIRouter()

@router.get("/{venta_id}", response_model=List[Response_detalle_venta])
def obtener_detalles_venta(venta_id: int, db: Session = Depends(get_db)):
    lista_detalles = obtener_detalles_por_venta(db=db, venta_id=venta_id)
    #Si la lista vuelve vacía, 404
    if not lista_detalles:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No se encontraron detalles para esta venta"
        )
    return lista_detalles