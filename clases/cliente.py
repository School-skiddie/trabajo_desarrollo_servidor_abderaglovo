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
    
    # Obtener el pedido
    def pedido_añadir(nombre_restaurante, pedido_nombre, categoria):
        for menu in restaurante.restaurantes_lista[nombre_restaurante][categoria][pedido_nombre]:
            print(f"{menu['nombre']} - Precio: {menu['precio']} €")
            lista_compra = {  }

    # Obtener saldo
    def saldo(usuario):
        for i in clientes_clase:
            if(usuario == i.nombre):
                return i.dinero

    # Obtener historial de compras
    def historial(usuario):
        contador=0
        for historial in historial_clientes.get(usuario):
            print (f"{contador} - {historial}")
            contador=contador+1

    # Ingresar dinero
    def ingreso(usuario, ingreso):
        for i in clientes_clase:
            if(usuario == i.nombre):
                i.dinero += ingreso
                clientes_lista[usuario]["saldo"] = clientes_lista[usuario]["saldo"]+ingreso
                base_de_datos.database.Usuarios.añadir_datos(clientes_lista)