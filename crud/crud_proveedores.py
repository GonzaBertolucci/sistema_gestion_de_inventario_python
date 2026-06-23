from sqlalchemy.orm import Session
from models.proveedor import Proveedor
from schemas.proveedor import Agregar_Proveedor

# C R U D proveedores


def agregar_nuevo_proveedor(db: Session, provedor_data: Agregar_Proveedor):
    nuevo_proveedor = Proveedor(nombre_Prov=provedor_data.nombre_Prov)

    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)

    return nuevo_proveedor


"""
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
"""
