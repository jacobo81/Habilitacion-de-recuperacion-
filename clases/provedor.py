
from clases.producto import Producto
from clases.usuario import Usuario


class Proveedor(Usuario):
    Productos:Producto[5]
    def __init__(self,productos:Producto[5]):
        ProductosProveedor:productos
    def SubirProductos (self,Productos:Producto[5]):
        pass
    def enviarOfertas (self,Productos:Producto[5]):
        pass