import clases.cliente
import json
from os import path

debug = True # activar el debug mode, para saber que esta haciendo

usuarios_json_file = "C:\\Users\\usuario\\Desktop\\trabajo_abderaglovo\\base_de_datos\\usuarios.json" # fichero json relativa

# Añadir los datos de los usuarios al json
def añadir_datos(datos):
    js = json.dumps(datos, sort_keys=True, indent=4, separators=(',', ': '))
    with open(usuarios_json_file, 'w+') as f:
        f.write(js)

# USUARIOS carga
def cargar_usuarios():
    # Comprobamos si existe
    if path.isfile(usuarios_json_file) is False:
        raise Exception("El archivo 'usuarios.json', no se ha encontrado, error...")
    
    with open(usuarios_json_file, "rb") as fp:
        datos = dict(json.load(fp))

    clases.cliente.clientes_lista.update(datos) # esto para la lista, hacemos un update para añadir los nuevos valores

    for carga in clases.cliente.clientes_lista.keys(): # mostramos todas las keys, y añadimos esto a la clase
        if(debug):
            print("\n[CARGA DE DATOS A LA CLASE]: ", carga, clases.cliente.clientes_lista[carga][0], clases.cliente.clientes_lista[carga][1], clases.cliente.clientes_lista[carga][2], "\n")
        
        registrar = clases.cliente.Cliente(carga, clases.cliente.clientes_lista[carga][0], clases.cliente.clientes_lista[carga][1], clases.cliente.clientes_lista[carga][2])
        clases.cliente.clientes_clase.append(registrar)
    
    if(debug):    
        print("\n[CARGA DE DATOS LISTA]: ",clases.cliente.clientes_lista,"\n") # pruebas debug
        print("\n[CARGA DE DATOS CLASE]: ",clases.cliente.clientes_clase,"\n") # pruebas debug

# Comprobacion de que el usuario existe,correo,telefono

def comprobacion_usuario_sesion(usuario, password):
    for i in clases.cliente.clientes_clase:
        if(usuario == i.nombre and password == i.password):
            if(debug):
                print("\n[COMPROBACION DE DATOS]: datos_correctos = True\n")
            return True

# Comprobacion de que el usuario existe para no añadir los datos

def existe_usuario(usuario, telefono, correo):
    for i in clases.cliente.clientes_clase:
        if(usuario == i.nombre or telefono == i.telefono or correo == i.correo):
            if(debug):
                print("\n[BASE DE DATOS CLASES]: el usuario existe\n")
            return True
