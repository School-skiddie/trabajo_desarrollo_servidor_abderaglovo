import funciones.funciones, base_de_datos.database, datetime, clases.cliente, random
from collections import defaultdict

restaurantes_clase = []
restaurantes_lista = {}
historial_restaurantes_temp = defaultdict(list) # esto es para que lo guarde temporalmente y luego lo elimine con un clear
historial_restaurantes = {}
pedidos_tramite = []

class Restaurante:
    def __init__(self, nombre, password, comidas, bebidas, postres, reputacion = 0):
        self.nombre = nombre
        self.password = password
        self.comidas = comidas
        self.bebidas = bebidas
        self.postres = postres
        self.reputacion = reputacion

    def aceptar_pedido(nombre, nombre_usuario):
        productos=""
        contador_productos=0
        for num_lista in clases.cliente.lista_compra.keys():
            productos+=f"Producto: {clases.cliente.lista_compra[num_lista]['producto']} | Precio: {clases.cliente.lista_compra[num_lista]['precio']} €, "
            contador_productos=contador_productos+10

        if(clases.cliente.Cliente.saldo(nombre_usuario) < clases.cliente.Cliente.pedido(True)):
            return print("[+] No tienes suficiente saldo para hacer este pedido") 


        historial_restaurantes_temp[nombre].append(f"[Usuario: {nombre_usuario}] Fecha: {datetime.date.today()} {productos} Total Pago: {clases.cliente.Cliente.pedido(True)} €")
        historial_restaurantes = historial_restaurantes_temp
        
        clases.cliente.historial_clientes_temp[nombre_usuario].append(f"Fecha: {datetime.date.today()} {productos} Total Pago: {clases.cliente.Cliente.pedido(True)} €")
        clases.cliente.historial_clientes = clases.cliente.historial_clientes_temp

        base_de_datos.database.Gerentes.añadir_pedido_historial(historial_restaurantes)

        base_de_datos.database.Usuarios.añadir_pedido_usuarios_historial(clases.cliente.historial_clientes)

        clases.cliente.Cliente.quitar_saldo(nombre_usuario, clases.cliente.Cliente.pedido(True))

        print(f"[+] El pedido se ha tramitado, tardará {'20' if contador_productos == 10 else contador_productos} minutos")
       
        pedidos_tramite.append(f"(Pedido: {len(pedidos_tramite)} en {'20' if contador_productos == 10 else contador_productos} minutos estará listo..), ")

        clases.cliente.lista_compra.clear()

    # Obtener historial de compras
    def historial(nombre):
        try:
            for mostrar in historial_restaurantes[nombre]:
                print (f"[+] - {mostrar}\n")
        except KeyError:
            print("[+] No se ha encontrado nada en su historial...")
    
    # Obtener menu del restaurante
    def menu(categoria, nombre):
        contador=0
        funciones.funciones.borrar_pantalla()
        for menu in restaurantes_lista[nombre][categoria]:
            print(f"{contador} - {menu['nombre']} - Precio: {menu['precio']} €")
            contador=contador+1






