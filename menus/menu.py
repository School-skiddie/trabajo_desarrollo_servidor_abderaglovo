import clases.cliente
import base_de_datos.database
import json
#---------------------------------------------------------------
def menu_principal():
        print("1 - Dar de alta como restaurante o usuario")
        print("2 - Iniciar sesión")

        seleccion = int(input(">"))

        if(seleccion == 1):
            print("1 - Dar de alta como gerente")
            print("2 - Dar de alta como usuario")
            seleccion_1 = int(input(">"))

            if(seleccion_1 == 1):
                nombre = input("Escribe el nombre del restaurante: ")
            elif(seleccion_1 == 2):
                # ------------------------------------------------ INPUTS
                usuario = input("Escriba el nombre de usuario: ")
                password = input("Escriba la contraseña: ")
                telefono = input("Escriba su teléfono: ")
                correo = input("Escriba su correo eléctronico: ")

                # ------------------------------------------------ LLAMADA DE LA CLASE

                # ------------------------------------------------ COMPROBACIONES
                usuario_registrado = False

                #for usuarios in clases.cliente.clientes_registrados:
                #    if(usuarios.telefono == telefono or usuarios.correo == correo or usuarios.nombre == usuario):
                #        usuario_registrado = True
                #    else:
                #        usuario_registrado = False
                    
                if(usuario_registrado):
                    print("¡El usuario ya se encuentra registrado!, puede ser que los datos como 'teléfono,correo o usuario' se encuentren duplicados")
                else:
                    # registra el nuevo usuario a la lista
                    registrar = clases.cliente.Cliente(usuario, password, telefono, correo)

                    clases.cliente.clientes_lista[usuario] = password, telefono, correo # esto para el dictionario

                    if(base_de_datos.database.existe_usuario(usuario, telefono, correo)):
                        print("Este usuario ya existe, prueba otro nombre")
                    else:
                        clases.cliente.clientes_clase.append(registrar) # registramos los nuevos valores a la clase

                        if(base_de_datos.database.debug):
                            print("\n[BASE DE DATOS CLASES]: añadido la base de datos a la lista\n")

                        base_de_datos.database.añadir_datos(clases.cliente.clientes_lista) # añadimos los nuevos valores al json
            
                        print("¡Se ha añadido a la base de datos correctamente!, ahora podra iniciar sesión")
        elif(seleccion == 2):
            print("1 - Iniciar sesión gerente")
            print("2 - Iniciar sesión como usuario")
            seleccion = int(input(">"))

            if(seleccion == 1):
                codigo = input("Introduce el código identificador del restaurante: ")
            elif(seleccion == 2):
                usuario = input("Introduce su usuario: ")
                password = input("Introduce su contraseña: ")

                if(base_de_datos.database.comprobacion_usuario_sesion(usuario, password)):
                    print("Has iniciado sesion")
        elif(seleccion == 3):
            pass
        elif(seleccion == 4):
            pass
#---------------------------------------------------------------

#---------------------------------------------------------------
def menu_usuario(sub_menu):
    print("1 - Hacer un pedido")
    print("2 - Añadir credito a la cuenta [Credito Actual: {}]")
    print("3 - Historial de pedidos")
    seleccion = input(">")

    if(seleccion == 1):
        pass
    elif(seleccion == 2):
        pass
    elif(seleccion == 3):
        pass
    elif(seleccion == 4):
        pass
         # BLA BLA BLA BLA
#---------------------------------------------------------------

#---------------------------------------------------------------
def menu_restaurante():
        print("1 - Consultar historial de pedidos")
        print("2 - Generar un cupón de descuento")
        print("3 - Añadir un nuevo menu")
        seleccion = input(">")

        if(seleccion == 1):
            pass
        elif(seleccion == 2):
            pass
        elif(seleccion == 3):
            print("1 - Comida")
            print("2 - Bebidas")
            print("3 - Postres")
        elif(seleccion == 4):
            pass

#---------------------------------------------------------------