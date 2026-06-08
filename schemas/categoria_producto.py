from pydantic import BaseModel


class Agregar_Categoria_Producto(BaseModel):
    nombre_Cat : str
    desc_Cat : str


class Response_Categoria_Producto(BaseModel):
    id_Cat : int
    nombre_Cat : str
    desc_Cat : str
    cat_Activo : bool

    class Config:
        from_attributes = True
