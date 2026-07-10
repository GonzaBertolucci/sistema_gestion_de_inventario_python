from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.ventas import VentasCreate, Response_venta, VentasUpdate
from crud.crud_ventas import crear_nueva_venta, obtener_todas_las_ventas, obtener_venta_por_id, actualizar_venta, eliminar_venta

router = APIRouter()

@router.post("/", response_model=Response_venta)
def registrar_venta(venta: VentasCreate, db: Session = Depends(get_db)):
    try:
        nueva_venta = crear_nueva_venta(db=db, venta_data=venta)
        return nueva_venta
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
        #El str(e) agarra el texto del CRUD

@router.get("/", response_model=List[Response_venta])
def leer_ventas(db: Session = Depends(get_db)):
    lista_de_ventas = obtener_todas_las_ventas(db=db)
    return lista_de_ventas

@router.get("/{ventas_id}", response_model=Response_venta)
def leer_venta_por_id(venta_id: int, db:Session = Depends(get_db)):
    venta = obtener_venta_por_id(db=db,venta_id=venta_id)
    
    if venta is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Venta no encontrada")
    return venta
    
@router.put("/{venta_id}", response_model=Response_venta)
def modificar_venta(venta_id: int, datos_nuevos: VentasUpdate, db: Session = Depends(get_db)):
    venta_actualizada = actualizar_venta(db=db, venta_id=venta_id, venta_actualizada=datos_nuevos)
    
    if venta_actualizada is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Venta a actualizar no encontrada")
    
    return venta_actualizada

@router.delete("/{venta_id}", response_model=Response_venta)
def borrar_venta(venta_id: int, db: Session = Depends(get_db)):
    venta_eliminada = eliminar_venta(db=db, venta_id=venta_id)
    
    if venta_eliminada is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "La venta a eliminar no existe")
    
    return venta_eliminada    
