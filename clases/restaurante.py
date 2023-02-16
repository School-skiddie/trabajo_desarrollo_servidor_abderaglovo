restaurantes_clase = []
restaurantes_lista = {}

class Restaurante:
    def __init__(self, nombre, password, comidas, bebidas, postres, cocineros, reputacion = 0):
        self.nombre = nombre
        self.password = password
        self.comidas = comidas
        self.bebidas = bebidas
        self.postres = postres
        self.cocineros = cocineros
        self.reputacion = reputacion

    def __str__(self):
        return 'nombre:{} reputacion:{}'.format(self.nombre,self.reputacion)

    def aceptar_pedido(self, pedido):
        self.pedido = pedido
        self.cuenta = 0

        for item in self.pedido:
            self.cuenta += item['precio']

        return self.cuenta        

    def cobrar_pedido(self):
        pass

    def asignar_cocinero(self):
        pass

    def preparar_pedido(self):
       pass  





