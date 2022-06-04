class Pedido ():
    PedidoID:str
    NombreCliente:Cliente
    IDcliente:Cliente
    NombreProveedor:Proveedor
    IDProveedor:Proveedor
    Productos:Producto[5]
    ValorProducto:Producto
    OfertaProducto:Producto
    ValorTotal:float
    Fechalimite:Fecha
    def __init__ (self,clientes:Cliente,proveedores:Proveedor,productos:Producto[5]):
        Clientes=clientes
        Proveedores=proveedores
        Productos=productos
    def GenerarPedido(self,PedidoID:str,NombreCliente:Cliente,IDcliente:Cliente,NombreProveedor:Proveedor, IDProveedor:Proveedor
    ,Productos:Producto[5], ValorProducto:Producto,OfertaProducto:Producto, ValorTotal:float, Fechalimite:Fecha):
        pass
    def EnviarPedido(self,PedidoID:str,NombreCliente:Cliente,IDcliente:Cliente,NombreProveedor:Proveedor, IDProveedor:Proveedor
    ,Productos:Producto[5], ValorProducto:Producto,OfertaProducto:Producto, ValorTotal:float, Fechalimite:Fecha):
        pass
    def CalcularValorTotal(self,Productos:Producto[5],ValorProducto:Producto):
        pass
