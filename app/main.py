from fastapi import FastAPI
from api.routes import usuarios
import models.usuario
import models.ventas
import models.detalles_de_ventas

app = FastAPI(title="Gestión de Inventario")

app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])


'''
# Incluyes las rutas separadas
app.include_router(proveedores.router, prefix="/proveedores", tags=["Proveedores"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
'''



