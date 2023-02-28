import funciones.funciones, base_de_datos.database, datetime, clases.cliente, clases.restaurante
from collections import defaultdict

import json

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
    
    def añadir_remover_menu(opcion, nombre):
        while True:
            funciones.funciones.borrar_pantalla()
            if(opcion): # añadir
                print("1 - Comidas")
                print("2 - Bebidas")
                print("3 - Postres\n")
                categoria = int(input("[+] Escriba el id de la categoria: "))
                if(categoria == 1):
                    categoria_nombre_extrapolado = "comidas"
                elif(categoria == 2):
                    categoria_nombre_extrapolado = "bebidas"
                elif(categoria == 3):
                    categoria_nombre_extrapolado = "postres"
                else:
                    print("[-] Esa categoria no existe, escribala de nuevo...")
                funciones.funciones.borrar_pantalla()
                nombre_producto = input("[+] Escriba el nombre del producto: ")
                precio_producto = float(input("[+] Escriba el precio el producto: "))

                base_de_datos.database.Gerentes.añadir_producto(nombre, categoria_nombre_extrapolado, nombre_producto, precio_producto)
                print("\n[+] El producto se ha añadido correctamente...\n")
                funciones.funciones.pausa()
            else:       # remover
                print("1 - Comidas")
                print("2 - Bebidas")
                print("3 - Postres\n")
                categoria = int(input("[+] Escriba el id de la categoria: "))

                categoria_nombre_extrapolado = ""

                if(categoria == 1):
                    categoria_nombre_extrapolado = "comidas"
                elif(categoria == 2):
                    categoria_nombre_extrapolado = "bebidas"
                elif(categoria == 3):
                    categoria_nombre_extrapolado = "postres"
                else:
                    print("[-] Esa categoria no existe, escribala de nuevo...")

                funciones.funciones.borrar_pantalla()
                contador=0
                for menu in restaurantes_lista[nombre][categoria_nombre_extrapolado]:
                    print(f"ID: {contador} - {menu['nombre']}")
                    contador=contador+1
                
                id_menu = int(input("[-] Escriba el ID del menu que desea eliminar: "))

                base_de_datos.database.Gerentes.remover_producto(id_menu, nombre, categoria_nombre_extrapolado)
                print("\n[+] El producto se ha eliminado correctamente...\n")
                funciones.funciones.pausa()







