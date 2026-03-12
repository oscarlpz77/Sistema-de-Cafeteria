from enum import Enum

class Temperatura(Enum):
    FRIA = "Fría"
    CALIENTE = "Caliente"

class Rol(Enum):
    BARISTA = "Barista"
    MESERO = "Mesero"
    GERENTE = "Gerente"

class EstadoPedido(Enum):
    PENDIENTE = "Pendiente"
    PREPARANDO = "Preparando"
    ENTREGADO = "Entregado"


class Persona:

    def __init__(self,idPersona,nombre,email):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email

    def login(self):
        print(self.nombre,"ha iniciado sesión")

    def actualizarPerfil(self,nombre,email):
        self.nombre=nombre
        self.email=email
        print("El perfil ha sido actualizado")


class Cliente(Persona):

    def __init__(self,idPersona,nombre,email):
        super().__init__(idPersona,nombre,email)
        self.puntosFidelidad=0
        self.historialPedidos=[]

    def realizarPedido(self,pedido):
        print("Realizando el pedido.")
        self.historialPedidos.append(pedido)
        print("El pedido se ha agregado al historial")

    def consultarHistorial(self):
        print("Historial de pedidos")
        for p in self.historialPedidos:
            print("Pedido:",p.idPedido,"Total:",p.total)

    def canjearPuntos(self):

        if self.puntosFidelidad >= 100:
            print("Canjeando puntos")
            self.puntosFidelidad = self.puntosFidelidad - 100
            print("Puntos restantes:",self.puntosFidelidad)
            return

        print("No tiene suficientes puntos")


class Empleado(Persona):

    def __init__(self,idPersona,nombre,email,idEmpleado,rol):
        super().__init__(idPersona,nombre,email)
        self.idEmpleado=idEmpleado
        self.rol=rol

    def actualizarInventario(self,inventario,ingrediente,cantidad):
        print("Actualizando inventario.")
        inventario.reducirStock(ingrediente,cantidad)

    def cambiarEstadoPedido(self,pedido,estado):
        pedido.estado=estado
        print("El estado del pedido ha cambiado a",estado)


class ProductoBase:

    def __init__(self,idProducto,nombre,precioBase,tipo):
        self.idProducto=idProducto
        self.nombre=nombre
        self.precioBase=precioBase
        self.tipo=tipo


class Bebida(ProductoBase):

    def __init__(self,idProducto,nombre,precioBase,tamaño,temperatura):
        super().__init__(idProducto,nombre,precioBase,"bebida")
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificadores=[]

    def agregarExtra(self,extra):
        print("Agregando extra:",extra)
        self.modificadores.append(extra)

    def calcularPrecioFinal(self):

        precio=self.precioBase

        numExtras=len(self.modificadores)

        precio=precio+(numExtras*5)

        print("Precio final de la bebida:",precio)

        return precio


class Postre(ProductoBase):

    def __init__(self,idProducto,nombre,precioBase,esVegano,sinGluten):
        super().__init__(idProducto,nombre,precioBase,"postre")
        self.esVegano=esVegano
        self.sinGluten=sinGluten


class Pedido:

    def __init__(self,idPedido):
        self.idPedido=idPedido
        self.productos=[]
        self.estado=EstadoPedido.PENDIENTE
        self.total=0

    def agregarProducto(self,producto):

        print("Agregando producto al pedido")

        self.productos.append(producto)

        print("Producto agregado:",producto.nombre)

    def calcularTotal(self):

        print("Calculando total del pedido")

        total=0

        for p in self.productos:

            if p.tipo == "bebida":
                total = total + p.calcularPrecioFinal()

            if p.tipo == "postre":
                total = total + p.precioBase

        self.total=total

        print("Total del pedido:",total)

    def validarStock(self,inventario):

        print("Validando stock del pedido")

        for p in self.productos:

            print("Verificando producto:",p.nombre)

            inventario.notificarFaltante(p.nombre)


class Inventario:

    def __init__(self):
        self.ingredientes={}

    def agregarIngrediente(self,nombre,cantidad):

        print("Agregando ingrediente:",nombre)

        self.ingredientes[nombre]=cantidad

    def reducirStock(self,nombre,cantidad):

        existe=False

        for ingrediente in self.ingredientes:
            if ingrediente==nombre:
                existe=True

        if existe==False:
            print("Ingrediente no encontrado")
            return

        if self.ingredientes[nombre] < cantidad:
            print("No hay suficiente ingrediente")
            return

        self.ingredientes[nombre]=self.ingredientes[nombre]-cantidad

        print("Stock actualizado")

    def notificarFaltante(self,nombre):

        for ingrediente in self.ingredientes:
            if ingrediente==nombre:
                if self.ingredientes[nombre] < 5:
                    print("El ingrediente",nombre,"se está terminando")
                    
                    
                    
                    
                    