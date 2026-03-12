from cafeteria import *

print("Inicio del Sistema de Cafetería")

print("Registro de clientes")

clientes = []
clientes.append(Cliente(1,"Andres Vega","andres.vega@gmail.com"))
clientes.append(Cliente(2,"Paola Cruz","paola.cruz@gmail.com"))
clientes.append(Cliente(3,"Javier Luna","javier.luna@gmail.com"))
clientes.append(Cliente(4,"Fernanda Rios","fernanda.rios@gmail.com"))
clientes.append(Cliente(5,"Roberto Salas","roberto.salas@gmail.com"))
clientes.append(Cliente(6,"Daniela Ortiz","daniela.ortiz@gmail.com"))
clientes.append(Cliente(7,"Hector Mendoza","hector.mendoza@gmail.com"))
clientes.append(Cliente(8,"Valeria Navarro","valeria.navarro@gmail.com"))
clientes.append(Cliente(9,"Adrian Castillo","adrian.castillo@gmail.com"))
clientes.append(Cliente(10,"Gabriela Soto","gabriela.soto@gmail.com"))

print("Clientes registrados:",len(clientes))

print("Registro de empleados")

empleados = []
empleados.append(Empleado(1,"Marco Alvarez","marco.alvarez@gmail.com",101,Rol.BARISTA))
empleados.append(Empleado(2,"Sergio Paredes","sergio.paredes@gmail.com",102,Rol.MESERO))
empleados.append(Empleado(3,"Alejandro Moreno","alejandro.moreno@gmail.com",103,Rol.GERENTE))
empleados.append(Empleado(4,"Bruno Castillo","bruno.castillo@gmail.com",104,Rol.BARISTA))
empleados.append(Empleado(5,"Ivan Herrera","ivan.herrera@gmail.com",105,Rol.MESERO))
empleados.append(Empleado(6,"Victor Mendoza","victor.mendoza@gmail.com",106,Rol.BARISTA))
empleados.append(Empleado(7,"Eduardo Vargas","eduardo.vargas@gmail.com",107,Rol.MESERO))
empleados.append(Empleado(8,"Oscar Rojas","oscar.rojas@gmail.com",108,Rol.BARISTA))
empleados.append(Empleado(9,"Ramon Salazar","ramon.salazar@gmail.com",109,Rol.MESERO))
empleados.append(Empleado(10,"Tomas Fuentes","tomas.fuentes@gmail.com",110,Rol.GERENTE))

print("Empleados registrados:",len(empleados))

print("Registro de bebidas")

bebidas = []
bebidas.append(Bebida(1,"Cafe Americano",35,"Mediano",Temperatura.CALIENTE))
bebidas.append(Bebida(2,"Latte",45,"Grande",Temperatura.CALIENTE))
bebidas.append(Bebida(3,"Capuccino",50,"Mediano",Temperatura.CALIENTE))
bebidas.append(Bebida(4,"Chocolate Caliente",40,"Grande",Temperatura.CALIENTE))
bebidas.append(Bebida(5,"Cafe Helado",42,"Grande",Temperatura.FRIA))
bebidas.append(Bebida(6,"Mocha",48,"Mediano",Temperatura.CALIENTE))
bebidas.append(Bebida(7,"Frappe",55,"Grande",Temperatura.FRIA))
bebidas.append(Bebida(8,"Te Verde",30,"Mediano",Temperatura.CALIENTE))
bebidas.append(Bebida(9,"Matcha Latte",60,"Grande",Temperatura.CALIENTE))
bebidas.append(Bebida(10,"Cold Brew",50,"Grande",Temperatura.FRIA))

print("Bebidas registradas:",len(bebidas))

print("Registro de postres")

postres = []
postres.append(Postre(1,"Pastel de Fresa",60,False,False))
postres.append(Postre(2,"Brownie Chocolate",45,False,False))
postres.append(Postre(3,"Galleta Chispas",20,False,False))
postres.append(Postre(4,"Flan Casero",35,False,False))
postres.append(Postre(5,"Pay de Limon",40,False,False))
postres.append(Postre(6,"Tarta de Queso",50,False,False))
postres.append(Postre(7,"Cupcake Vainilla",30,False,False))
postres.append(Postre(8,"Donut Azucar",25,False,False))
postres.append(Postre(9,"Muffin Arandanos",40,False,False))
postres.append(Postre(10,"Gelatina Frutas",18,True,True))

print("Postres registrados:",len(postres))

print("Inicializando inventario")

inventario = Inventario()
inventario.agregarIngrediente("Cafe",20)
inventario.agregarIngrediente("Leche",15)
inventario.agregarIngrediente("Chocolate",10)
inventario.agregarIngrediente("Azucar",25)
inventario.agregarIngrediente("Crema",8)
inventario.agregarIngrediente("Harina",12)
inventario.agregarIngrediente("Mantequilla",7)
inventario.agregarIngrediente("Matcha",6)
inventario.agregarIngrediente("Hielo",30)
inventario.agregarIngrediente("Vainilla",4)

print("Creación de pedidos")

pedidos = []
pedido1 = Pedido(1)
pedido1.agregarProducto(bebidas[0])
pedido1.agregarProducto(postres[0])
pedido1.calcularTotal()

pedidos.append(pedido1)

print("Prueba de metodos del Sistema")

clientes[0].login()
clientes[0].realizarPedido(pedido1)
clientes[0].consultarHistorial()

empleados[0].actualizarInventario(inventario,"Cafe",2)
empleados[1].cambiarEstadoPedido(pedido1,EstadoPedido.PREPARANDO)

clientes[0].actualizarPerfil("Andres Vega Gomez","andres.nuevo@gmail.com")

clientes[0].puntosFidelidad = 120
clientes[0].canjearPuntos()

bebidas[0].agregarExtra("Leche de almendra")
bebidas[0].agregarExtra("Sin azucar")
bebidas[0].calcularPrecioFinal()

pedido1.validarStock(inventario)

print("Datos del cliente")

print("ID:",clientes[0].idPersona)
print("Nombre:",clientes[0].nombre)
print("Email:",clientes[0].email)
print("Puntos:",clientes[0].puntosFidelidad)

print("Fin del sistema")