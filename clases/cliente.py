 ducto, ValorTotal:float, Fechalimite:Fecha):
        pass
    def CalcularValorTotal(self,Productos:Producto[5],ValorProducto:Producto):
        pass
from Clases.pedido import Pedido
from Clases.usuario import Usuario
from producto import Producto


class Cliente (Usuario):
    Direccion:str
    IDCliente:str
    Productos:Producto[5]
    Pedidos:Pedido[5]
    def CrearCliente (self,Direccion:str,IDCliente:str):
        pass
    def ModificarCliente (self,Direccion:str,IDCliente:str):
        pass
    def EnviarOferta (self,Productos:Producto[5]):
        pass
    def ConsultarOferta (self,Productos:Producto[5]):
        pass
    def HacerPeddido (self,Pedidos:Pedido[5]):
        pass
