from fastapi import FastAPI
from api.routes import usuarios, ventas
import models.usuario
import models.ventas
import models.detalles_de_ventas
import models.producto
import models.proveedor
import models.categoria_producto

app = FastAPI(title="Gestión de Inventario")

app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])

app.include_router(ventas.router, prefix="/ventas", tags=["Ventas"])


'''
# Incluyes las rutas separadas
app.include_router(proveedores.router, prefix="/proveedores", tags=["Proveedores"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])
'''



