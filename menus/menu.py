import clases.cliente, clases.restaurante, base_de_datos.database, funciones.funciones, getpass

#---------------------------------------------------------------
def menu_principal():
    while True:
        print("1 - Dar de alta como restaurante o usuario")
        print("2 - Iniciar sesión")

        seleccion = int(input(">"))

        if(seleccion == 1):
            print("1 - Dar de alta como gerente")
            print("2 - Dar de alta como usuario")
            while True:
                try:
                    seleccion_1 = int(input(">"))
                    break
                except ValueError:
                    print("Opcion desconocida..., por favor inserte otra vez su seleccion")

            if(seleccion_1 == 1):
                # ------------------------------------------------ INPUTS
                nombre = input("Escriba el nombre del restaurante: ")
                password = getpass.getpass("Escriba la contraseña: ")
            
                # ------------------------------------------------ COMPROBACIONES
                if(base_de_datos.database.Gerentes.existe_restaurante(nombre)):
                    print("¡El restaurante ya se encuentra registrado!, intente con otro nombre")
                else:
                    # registra el nuevo usuario a la lista
                    registrar = clases.restaurante(nombre, password)
                    
                    clases.restaurante.restaurantes_lista[nombre] = { "password": password } # esto para el dictionario

                    clases.restaurante.restaurantes_clase.append(registrar) # registramos los nuevos valores a la clase

                    if(base_de_datos.database.debug):
                        print("\n[BASE DE DATOS CLASES]: añadido la base de datos a la lista\n")

                    base_de_datos.database.Gerentes.añadir_datos(clases.cliente.restaurantes_lista) # añadimos los nuevos valores al json
            
                    print("\n¡Se ha añadido a la base de datos correctamente!, ahora podra iniciar sesión\n")
                    funciones.funciones.pausa()
                    funciones.funciones.borrar_pantalla()
            elif(seleccion_1 == 2):
                # ------------------------------------------------ INPUTS
                usuario = input("Escriba el nombre de usuario: ")
                password = getpass.getpass("Escriba la contraseña: ")
                while True:
                    try:
                        telefono = int(input("Escriba su teléfono: "))
                        break
                    except ValueError:
                        print("\n(Incorrecto) Escriba otra vez el número")

                while True:
                    correo = input("Escriba su correo eléctronico: ")
                    if(funciones.funciones.email_es_valido(correo)):
                        break
                    else:
                        print("\n(Incorrecto) El e-mail no es valido, escribalo de nuevo")

                # ------------------------------------------------ COMPROBACIONES
                if(base_de_datos.database.Usuarios.existe_usuario(usuario, telefono, correo)):
                    print("¡El usuario ya se encuentra registrado!, puede ser que los datos como 'teléfono,correo o usuario' se encuentren duplicados")
                else:
                    # registra el nuevo usuario a la lista
                    registrar = clases.cliente.Cliente(usuario, password, telefono, correo)
                    
                    clases.cliente.clientes_lista[usuario] = { "password": password, "telefono": telefono, "correo": correo, "saldo": 1000 } # esto para el dictionario

                    clases.cliente.clientes_clase.append(registrar) # registramos los nuevos valores a la clase

                    if(base_de_datos.database.debug):
                        print("\n[BASE DE DATOS CLASES]: añadido la base de datos a la lista\n")

                    base_de_datos.database.Usuarios.añadir_datos(clases.cliente.clientes_lista) # añadimos los nuevos valores al json
            
                    print("\n¡Se ha añadido a la base de datos correctamente!, ahora podra iniciar sesión\n")
                    funciones.funciones.pausa()
                    funciones.funciones.borrar_pantalla()
        elif(seleccion == 2):
            print("1 - Iniciar sesión gerente")
            print("2 - Iniciar sesión como usuario")
            while True:
                try:
                    seleccion = int(input(">"))
                    break
                except ValueError:
                    print("Opcion desconocida..., por favor inserte otra vez su seleccion")

            if(seleccion == 1):
                nombre = input("\nIntroduce el nombre del restaurante: ")
                password = getpass.getpass("\nIntroduce la contraseña: ")

                # ------------------------------------------------ COMPROBACIONES
                if(base_de_datos.database.Gerentes.comprobacion_gerente_sesion(nombre, password)):
                    print(f"\nHas iniciado sesion como gerente de {nombre}\n")
                    menu_restaurante(nombre)
                else:
                    print("\nDatos incorrectos, intentelo de nuevo\n")
            elif(seleccion == 2):
                usuario = input("\nIntroduce su usuario: ")
                password = getpass.getpass("\nIntroduce la contraseña: ")

                # ------------------------------------------------ COMPROBACIONES
                if(base_de_datos.database.Usuarios.comprobacion_usuario_sesion(usuario, password)):
                    print(f"\nHas iniciado sesion como {usuario}\n")
                    menu_usuario(usuario)
                else:
                    print("\nDatos incorrectos, intentelo de nuevo\n")
        elif(seleccion == 3):
            pass
        elif(seleccion == 4):
            pass
#---------------------------------------------------------------

#---------------------------------------------------------------
def menu_usuario(usuario):
    while True:
        print("1 - Hacer un pedido")
        print(f"2 - Añadir credito a la cuenta [Credito Actual: {clases.cliente.Cliente.saldo(usuario)}]")
        print("3 - Historial de pedidos")
        while True:
            try:
                seleccion = int(input(">"))
                break
            except ValueError:
                print("Opcion desconocida..., por favor inserte otra vez su seleccion")

        if(seleccion == 1):
            base_de_datos.database.Gerentes.restaurantes()
        elif(seleccion == 2):
            while True:
                cantidad = float(input("Inserte la cantidad, minimo 5.00 €: "))
                if(cantidad < 5.00):
                    print("(Error) El minimo de cantidad a ingresar es de 5.00 €")
                else:
                    break
            
            print("\nNumero de la tarjeta de credito 4XXXXXXXX......: ")
            print("\nFecha caducidad X/XX: ")
            print("\nCCV de la tarjeta de credito XXX: ")
            clases.cliente.Cliente.ingreso(usuario, cantidad)
            print(f"\n[+] Se ha hecho un ingreso de {cantidad} a su cuenta.")
        elif(seleccion == 3):
            clases.cliente.Cliente.historial(usuario)

        funciones.funciones.pausa()
        funciones.funciones.borrar_pantalla()
         # BLA BLA BLA BLA
#---------------------------------------------------------------

#---------------------------------------------------------------
def menu_restaurante(nombre):
    while True:
        print("1 - Consultar historial de pedidos")
        print("2 - Generar un cupón de descuento")
        print("3 - Añadir un nuevo menu")
        seleccion = int(input(">"))

        if(seleccion == 1):
            clases.cliente.restaurante.Restaurante.historial(nombre)
        elif(seleccion == 2):
            pass
        elif(seleccion == 3):
            print("1 - Comida")
            print("2 - Bebidas")
            print("3 - Postres")
        elif(seleccion == 4):
            pass

        funciones.funciones.pausa()
        funciones.funciones.borrar_pantalla()

#---------------------------------------------------------------