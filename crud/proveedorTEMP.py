from fastapi import FastAPI,Depends
from sqlalchemy import String, select
from sqlalchemy.orm import Session

from db.database import SessionLocal
import models.models as models
import schemas.schemas as schemas

# C R U D temporal proveedores

app = FastAPI()
db = SessionLocal()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/proveedores/", response_model=schemas.Response_Proovedor)

def Agregar_proveedor (provedor: schemas.Agregar_Proveedor,db: Session = Depends(get_db)):
   Nuevo_proveedor = models.Proveedor(
    nombre_Prov = provedor.nombre_Prov
   )
   db.add(Nuevo_proveedor)
   db.commit()
   db.refresh(Nuevo_proveedor)
   return Nuevo_proveedor

'''
def showProveedor():
    # aca va el get
    buscarId = 1
    stmt = select(Proveedor).where(Proveedor.id_Prov == 0)
    print(db.get(Proveedor.id_Prov==0))
    db.commit()
    db.close()
    #listaProveedores = [""]
    

class updateProveedor:
    print("Proveedor modificado correctamente")


class deleteProveedor:
    #Aca va el modificar
    print("Se elimino el Proveedor correctamente")
'''