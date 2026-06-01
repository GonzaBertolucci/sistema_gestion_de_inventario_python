from database import SessionLocal
from models import Usuario
from models import Proveedor


db = SessionLocal()

usuario_prueba = Usuario(
  nombre_usuario = "Gonza",
  contrasenia_usuario = "contra_123",
  rol_usuario = True,
  activo = True
)

usuario_prueba2 = Usuario(
  nombre_usuario = "Tuyu",
  contrasenia_usuario = "contra_123",
  rol_usuario = True,
  activo = False
)

addProv = Proveedor(
    nombre_Prov = "Pepsico"
)

'''
db.add(usuario_prueba)
db.commit()
db.close()
print("Usuario1 agregado correctamente...")

db.add(usuario_prueba2)
db.commit()
db.close()
print("Usuario2 agregado correctamente...")
'''

db.add(addProv)
db.commit()
db.close()
print("Se añadio correctamente el proovedor")