from random import randint
from clases import menu
from clases import restaurante

clientes_clase = []
clientes_lista = {}

class Cliente:
    def __init__(self, nombre, password, correo, telefono, dinero = 1000):
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

    def consultar_saldo(self):
        return self.dinero
