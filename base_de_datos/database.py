import clases.cliente, clases.restaurante, json, os
from os import path

debug = False # activar el debug mode, para saber que esta haciendo

restaurantes_json_file = f"{os.getcwd()}\\json\\restaurantes.json" # fichero json relativa
restaurantes_historial = f"{os.getcwd()}\\json\\historial_restaurantes.json" # fichero json relativa

usuarios_json_file = f"{os.getcwd()}\\json\\usuarios.json" # fichero json relativa
usuarios_historial = f"{os.getcwd()}\\json\\historial_usuarios.json" # fichero json relativa

class Gerentes():
    # Añadir los datos del historial al json
    def añadir_pedido_historial(datos):
        js = json.dumps(datos, sort_keys=True, indent=4, separators=(',', ': '))
        with open(restaurantes_historial, 'w+') as f:
            f.write(js)

    # Añadir los datos de los gerentes al json
    def añadir_datos(datos):
        js = json.dumps(datos, sort_keys=True, indent=4, separators=(',', ': '))
        with open(restaurantes_json_file, 'w+') as f:
            f.write(js)

    def añadir_producto(nombre_restaurante, categoria, nombre_producto, precio_producto):
        with open(restaurantes_json_file, "rb") as fp:
            datos = dict(json.load(fp))

        lista_temporal=[]   

        for a in datos[nombre_restaurante][categoria]:
            lista_temporal.append(a)                    # lo guardamos en una lista para las posiciones

        lista_temporal.append({"nombre": nombre_producto, "precio": precio_producto})

        datos[nombre_restaurante][categoria] = lista_temporal

        js = json.dumps(datos, sort_keys=True, indent=4, separators=(',', ': '))
        with open(restaurantes_json_file, 'w') as f:                                # luego actualizamos
            f.write(js)

        Gerentes.cargar_restaurantes()  # actualizamos los restaurantes

    def remover_producto(menu, nombre_restaurante, categoria):
        with open(restaurantes_json_file, "rb") as fp:
            datos = dict(json.load(fp))

        lista_temporal=[]   

        for a in datos[nombre_restaurante][categoria]:
            lista_temporal.append(a)                    # lo guardamos en una lista para las posiciones

        lista_temporal.pop(menu)

        datos[nombre_restaurante][categoria] = lista_temporal

        js = json.dumps(datos, sort_keys=True, indent=4, separators=(',', ': '))
        with open(restaurantes_json_file, 'w') as f:                                # luego actualizamos
            f.write(js)

        Gerentes.cargar_restaurantes()  # actualizamos los restaurantes

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
            print("\n[CARGA DE DATOS HISTORIAL]: ", clases.restaurante.historial_restaurantes,"\n") # pruebas debug

        clases.restaurante.historial_restaurantes_temp.update(clases.restaurante.historial_restaurantes)

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
        for restaurantes in clases.restaurante.restaurantes_lista.keys():
            print (f"- {restaurantes}")

class Usuarios():

    # Añadir los datos del historial al json
    def añadir_pedido_usuarios_historial(datos):
        js = json.dumps(datos, sort_keys=True, indent=4, separators=(',', ': '))
        with open(usuarios_historial, 'w+') as f:
            f.write(js)

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

        clases.cliente.historial_clientes_temp.update(clases.cliente.historial_clientes)

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