import clases.cliente, clases.restaurante, json
from os import path

debug = True # activar el debug mode, para saber que esta haciendo

restaurantes_json_file = "C:\\Users\\usuario\\Desktop\\abderaglovo\\trabajo_daw_abderaglovo\\json\\restaurantes.json" # fichero json relativa
restaurantes_historial = "C:\\Users\\usuario\\Desktop\\abderaglovo\\trabajo_daw_abderaglovo\\json\\historial_restaurantes.json" # fichero json relativa

usuarios_json_file = "C:\\Users\\usuario\\Desktop\\abderaglovo\\trabajo_daw_abderaglovo\\json\\usuarios.json" # fichero json relativa
usuarios_historial = "C:\\Users\\usuario\\Desktop\\abderaglovo\\trabajo_daw_abderaglovo\\json\\historial_usuarios.json" # fichero json relativa

class Gerentes():
    # Añadir los datos de los usuarios al json
    def añadir_datos(datos):
        js = json.dumps(datos, sort_keys=True, indent=4, separators=(',', ': '))
        with open(restaurantes_json_file, 'w+') as f:
            f.write(js)

    # RESTAURANTES carga
    def cargar_restaurantes():
        # Comprobamos si existe
        if path.isfile(restaurantes_json_file) is False:
            raise Exception("El archivo 'restaurantes.json', no se ha encontrado, error...")
        
        with open(restaurantes_json_file, "rb") as fp:
            datos = dict(json.load(fp))

        clases.restaurante.restaurantes_lista.update(datos) # esto para la lista, hacemos un update para añadir los nuevos valores

        for carga in clases.restaurante.restaurantes_lista.keys(): # mostramos todas las keys, y añadimos esto a la clase
            if(debug):
                print("\n[CARGA DE DATOS A LA CLASE]: ", carga + "\n")
            
            registrar = clases.restaurante.Restaurante(carga, 
            clases.restaurante.restaurantes_lista[carga]['password'], 
            clases.restaurante.restaurantes_lista[carga]['comidas'], 
            clases.restaurante.restaurantes_lista[carga]['bebidas'], 
            clases.restaurante.restaurantes_lista[carga]['postres'], 
            clases.restaurante.restaurantes_lista[carga]['cocineros'], 
            clases.restaurante.restaurantes_lista[carga]['reputacion'])

            clases.restaurante.restaurantes_clase.append(registrar)
        
        if(debug):    
            print("\n[CARGA DE DATOS LISTA (RESTAURANTES)]: ",clases.restaurante.restaurantes_lista,"\n") # pruebas debug
            print("\n[CARGA DE DATOS CLASE (RESTAURANTES)]: ",clases.restaurante.restaurantes_clase,"\n") # pruebas debug

    def cargar_historial_restaurantes():
        # Comprobamos si existe
        if path.isfile(restaurantes_historial) is False:
            raise Exception("El archivo 'historial.json', no se ha encontrado, error...")
        
        with open(restaurantes_historial, "rb") as fp:
            datos = dict(json.load(fp))

        clases.restaurante.historial_restaurantes.update(datos) # esto para la lista, hacemos un update para añadir los nuevos valores
        
        if(debug):    
            print("\n[CARGA DE DATOS HISTORIAL]: ",clases.restaurante.historial_restaurantes,"\n") # pruebas debug

    # Comprobacion de que el usuario existe,nombre
    def comprobacion_gerente_sesion(restaurante, password):
        for i in clases.cliente.restaurante.restaurantes_clase:
            if(restaurante == i.nombre and password == i.password):
                if(debug):
                    print("\n[COMPROBACION DE DATOS (RESTAURANTES)]: datos_correctos = True\n")
                return True

    # Comprobacion de que el restaurante existe para no añadir los datos
    def existe_restaurante(nombre):
        for i in clases.restaurante.restaurantes_clase:
            if(nombre == i.nombre):
                if(debug):
                    print("\n[BASE DE DATOS CLASES (RESTAURANTES)]: el restaurante existe\n")
                return True
    
    def restaurantes():
        contador=0
        for restaurantes in clases.restaurante.restaurantes_lista.keys():
            print (f"{contador} - {restaurantes}")
            contador=contador+1

class Usuarios():
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
                print("\n[CARGA DE DATOS A LA CLASE]: ", carga, clases.cliente.clientes_lista[carga]['password'], clases.cliente.clientes_lista[carga]['telefono'], clases.cliente.clientes_lista[carga]['correo'], clases.cliente.clientes_lista[carga]['saldo'], "\n")
            
            registrar = clases.cliente.Cliente(carga, 
            clases.cliente.clientes_lista[carga]['password'], 
            clases.cliente.clientes_lista[carga]['telefono'], 
            clases.cliente.clientes_lista[carga]['correo'], 
            clases.cliente.clientes_lista[carga]['saldo'])

            clases.cliente.clientes_clase.append(registrar)
        
        if(debug):    
            print("\n[CARGA DE DATOS LISTA]: ",clases.cliente.clientes_lista,"\n") # pruebas debug
            print("\n[CARGA DE DATOS CLASE]: ",clases.cliente.clientes_clase,"\n") # pruebas debug

    # HISTORIAL usuarios carga
    def cargar_historial_usuarios():
        # Comprobamos si existe
        if path.isfile(usuarios_historial) is False:
            raise Exception("El archivo 'historial.json', no se ha encontrado, error...")
        
        with open(usuarios_historial, "rb") as fp:
            datos = dict(json.load(fp))

        clases.cliente.historial_clientes.update(datos) # esto para la lista, hacemos un update para añadir los nuevos valores
        
        if(debug):    
            print("\n[CARGA DE DATOS HISTORIAL]: ",clases.cliente.historial_clientes,"\n") # pruebas debug

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