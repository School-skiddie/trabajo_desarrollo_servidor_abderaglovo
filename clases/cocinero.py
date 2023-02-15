
class Cocinero:
    def __init__(self, nombre, experiencia, energia = 100):
        self.nombre = nombre
        self.experiencia = experiencia
        self.energia = energia
    
    def __str__(self):
        return 'nombre:{} experiencia:{} energia:{}'.format(self.nombre,self.experiencia, self.energia)

    def cocinar(self):
        pass