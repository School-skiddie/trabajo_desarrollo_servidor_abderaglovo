import funciones.funciones, base_de_datos.database, datetime, clases.cliente, random
restaurantes_clase = []
restaurantes_lista = {}
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

    def asignar_cocinero(self):
        pass

    def preparar_pedido(self):
       pass  

    def aceptar_pedido(nombre, nombre_usuario):
        productos=""
        contador_productos=0
        for num_lista in clases.cliente.lista_compra.keys():
            productos+=f"Producto: {clases.cliente.lista_compra[num_lista]['producto']} | Precio: {clases.cliente.lista_compra[num_lista]['precio']} €, "
            contador_productos=contador_productos+10
        historial_restaurantes[nombre] = f"Fecha: {datetime.date.today()} {productos} Total Pago: {clases.cliente.Cliente.pedido(True)} €"

        base_de_datos.database.Gerentes.añadir_pedido_historial(historial_restaurantes)

        historial_restaurantes.clear()

        historial_restaurantes[nombre_usuario] = f"Fecha: {datetime.date.today()} {productos} Total Pago: {clases.cliente.Cliente.pedido(True)} €"

        base_de_datos.database.Usuarios.añadir_pedido_usuarios_historial(historial_restaurantes)

        clases.cliente.Cliente.quitar_saldo(nombre_usuario, clases.cliente.Cliente.pedido(True))

        print(f"[+] El pedido se ha tramitado, tardará {'20' if contador_productos == 10 else contador_productos} minutos")
       
        pedidos_tramite.append(f"(Pedido: {len(pedidos_tramite)} En {'20' if contador_productos == 10 else contador_productos} minutos), ")

        funciones.funciones.pausa()

    # Obtener historial de compras
    def historial(nombre):
        contador=0
        for historial in historial_restaurantes.get(nombre):
            print (f"{contador} - {historial}")
            contador=contador+1
    
    # Obtener menu del restaurante
    def menu(categoria, nombre):
        contador=0
        funciones.funciones.borrar_pantalla()
        for menu in restaurantes_lista[nombre][categoria]:
            print(f"{contador} - {menu['nombre']} - Precio: {menu['precio']} €")
            contador=contador+1






