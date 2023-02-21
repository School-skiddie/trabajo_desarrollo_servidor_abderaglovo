from random import randint
from clases import menu,restaurante
import base_de_datos.database

clientes_clase = []
clientes_lista = {}
historial_clientes = {}

class Cliente:
    def __init__(self, nombre, password, correo, telefono, dinero = 1000.0):
        self.nombre = nombre
        self.password = password
        self.correo = correo
        self.telefono = telefono
        self.dinero = dinero

    def __str__(self):
        return 'nombre:{} distancia:{} dinero:{}'.format(self.nombre,self.distancia, self.dinero)

    def elegir_menu(self):
        comida = menu['comidas'][randint(0,3)]
        bebida = menu['bebidas'][randint(0,3)]
        postre = menu['postres'][randint(0,3)]
        
        self.pedido = [comida, bebida, postre]   

        self.enviar_pedido()

        print(self.pedido) 
        print(self.cuenta)
        
    def enviar_pedido(self):
        self.restaurante = restaurante('Pippo')
        self.cuenta = self.restaurante.aceptar_pedido(self.pedido)

    def recibir_pedido(self, entrega):
        pass

    def modificar_saldo(self):
        pass

    # Obtener saldo
    def saldo(usuario):
        for i in clientes_clase:
            if(usuario == i.nombre):
                return i.dinero

    # Obtener historial de compras
    def historial(usuario):
        for historial in historial_clientes.get(usuario):
            print (historial)

    # Ingresar dinero
    def ingreso(usuario, ingreso):
        for i in clientes_clase:
            if(usuario == i.nombre):
                i.dinero += ingreso
                clientes_lista[usuario]["saldo"] = clientes_lista[usuario]["saldo"]+ingreso
                base_de_datos.database.Usuarios.añadir_datos(clientes_lista)