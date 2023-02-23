from random import randint
from clases import menu,restaurante
import base_de_datos.database

clientes_clase = []
clientes_lista = {}
historial_clientes = {}

lista_compra = {} # Aqui guardaremos la lista de la compra

class Cliente:
    def __init__(self, nombre, password, correo, telefono, dinero = 1000.0):
        self.nombre = nombre
        self.password = password
        self.correo = correo
        self.telefono = telefono
        self.dinero = dinero
    
    # Completar pedido
    def completar_pedido():
        pass

    # Obtener pedido
    def pedido(preciototal):
        precio_total = 0
        for num_lista in lista_compra.keys():
            if(preciototal == False):
                print (f"[+] {lista_compra[num_lista]['producto']} - Precio: {lista_compra[num_lista]['precio']} €")
            precio_total=precio_total+lista_compra[num_lista]['precio']
        
        if(preciototal == False):    
            print(f"\n[+] Precio total: {precio_total} €")
        else:
            return precio_total
        

    # Añadir pedido
    def pedido_añadir(nombre_restaurante, pedido_nombre, categoria):
        seleccion = restaurante.restaurantes_lista[nombre_restaurante][categoria][pedido_nombre]

        cantidad = int(input("\n[+] Inserte la cantidad: "))

        #print (f"\n[+] Producto: {seleccion['nombre'] if cantidad < 1 else seleccion['nombre'] + f' x {cantidad}'} - Precio total: {seleccion['precio'] * cantidad} €")
        
        lista_compra[len(lista_compra)] = { 
            "producto": f"{seleccion['nombre'] if cantidad < 1 else seleccion['nombre'] + f' x {cantidad}'}", 
            "precio": float(seleccion['precio'] * cantidad) 
        }

    # Obtener saldo
    def saldo(usuario):
        for i in clientes_clase:
            if(usuario == i.nombre):
                return i.dinero

    # Obtener historial de compras
    def historial(usuario):
        print (f"[+] - {historial_clientes[usuario]}")

    # Quitar dinero
    def quitar_saldo(usuario, ingreso):
        for i in clientes_clase:
            if(usuario == i.nombre):
                i.dinero -= ingreso
                clientes_lista[usuario]["saldo"] = clientes_lista[usuario]["saldo"]-ingreso
                base_de_datos.database.Usuarios.añadir_datos(clientes_lista)

    # Ingresar dinero
    def ingreso(usuario, ingreso):
        for i in clientes_clase:
            if(usuario == i.nombre):
                i.dinero += ingreso
                clientes_lista[usuario]["saldo"] = clientes_lista[usuario]["saldo"]+ingreso
                base_de_datos.database.Usuarios.añadir_datos(clientes_lista)