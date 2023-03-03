import base_de_datos.database
import clases.restaurante
import clases.cliente
import clases.restaurante
import os
import tkinter
import funciones.funciones
import time

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, ttk, Checkbutton, BooleanVar, StringVar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(f"{os.getcwd()}\\theme\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

ventana = Tk()

def registrar_funcion(nombre, password, telefono, correo, gerente):

    if(not nombre or not password and gerente):
        Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                                background="#dc3e3e", text="Error, los campos se encuentran vacios...").place(x=30.0,
                                                                                                               y=30.0,
                                                                                                               width=400.0,
                                                                                                               height=43.0)
    else:
        if(not nombre or not password or not telefono or not correo and not gerente):
            Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                                    background="#dc3e3e", text="Error, los campos se encuentran vacios...").place(x=30.0,
                                                                                                                y=30.0,
                                                                                                                width=400.0,
                                                                                                                height=43.0)
        else:
            if (gerente):
                if (base_de_datos.database.Gerentes.existe_restaurante(nombre)):
                    error_texto = Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                                        background="#dc3e3e", text="Error, el nombre ya se encuentra registrado...").place(x=30.0,
                                                                                                                    y=30.0,
                                                                                                                    width=400.0,
                                                                                                                    height=43.0)
                else:
                    registrar = clases.restaurante.Restaurante(
                        nombre, password, "", "", "", 0)

                    clases.restaurante.restaurantes_lista[nombre] = {
                        "bebidas": [{}],
                        "comidas": [{}],
                        "postres": [{}],
                        "reputacion": 0,
                        "password": password}  # esto para el dictionario

                    # registramos los nuevos valores a la clase
                    clases.restaurante.restaurantes_clase.append(registrar)

                    base_de_datos.database.Gerentes.añadir_datos(
                        clases.restaurante.restaurantes_lista)  # añadimos los nuevos valores al json
                    Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                                        background="#6aa84f", text="Se ha completado, en 5 segundos....").place(x=30.0,
                                                                                                                    y=30.0,
                                                                                                                    width=400.0,
                                                                                                                    height=43.0)
                    menu_principal_grafico_inicio_sesion() # Milliseconds and then a function        
            else:
                if(not funciones.funciones.email_es_valido(correo)):
                    Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                                        background="#dc3e3e", text="Error, el correo es invalido...").place(x=30.0,
                                                                                                                    y=30.0,
                                                                                                                    width=400.0,
                                                                                                                    height=43.0)
                else:
                    if (base_de_datos.database.Usuarios.existe_usuario(nombre, telefono, correo)):
                        Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                                            background="#dc3e3e", text="Error, el nombre ya se encuentra registrado...").place(x=30.0,
                                                                                                                        y=30.0,
                                                                                                                        width=400.0,
                                                                                                                        height=43.0)
                    else:
                        # registra el nuevo usuario a la lista
                        registrar = clases.cliente.Cliente(
                            nombre, password, telefono, correo)

                        clases.cliente.clientes_lista[nombre] = {
                            "password": password, "telefono": telefono, "correo": correo, "saldo": 1000}  # esto para el dictionario

                        # registramos los nuevos valores a la clase
                        clases.cliente.clientes_clase.append(registrar)

                        base_de_datos.database.Usuarios.añadir_datos(
                            clases.cliente.clientes_lista)  # añadimos los nuevos valores al json
                        Label(ventana, font=('Purple Smile', 20), fg="#ffffff",
                                        background="#6aa84f", text="Se ha completado, en 5 segundos....").place(x=30.0,
                                                                                                                    y=30.0,
                                                                                                                    width=300.0,
                                                                                                                    height=43.0)
                        menu_principal_grafico_inicio_sesion() # Milliseconds and then a function   


def menu_principal_grafico_registro(gerente):  # registro
    ventana.geometry(f"450x{'420' if gerente else '600'}")
    ventana.configure(bg="#FFFFFF")
    ventana.title("registro")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=600,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_registrarse.png"))

    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: registrar_funcion(usuario.get(), contraseña.get(), "" if gerente else telefono.get(), "" if gerente else correo.get(), gerente),
        relief="flat"
    ).place(x=94.0,
            y=325 if gerente else 520,
            width=262.0,
            height=43.0
            )

    Label(ventana, font=('Purple Smile', 20),
          text="Usuario", bg="#FFFFFF").place(x=94.0,
                                              y=100.0)

    usuario = Entry(ventana, font=('Purple Smile', 20), background="#007FFF", fg="white")
    usuario.place(x=94.0,
                  y=150.0,
                  width=262.0,
                  height=43.0)

    Label(ventana, font=('Purple Smile', 20), text="Contraseña", bg="#FFFFFF").place(x=94.0,
                                                                               y=200.0)
    
    contraseña = Entry(ventana, font=('Purple Smile', 20),
                        background="#007FFF", fg="white", show="*")
    contraseña.place(x=94.0,
                        y=250.0,
                        width=262.0,
                        height=43.0)

    if(not gerente):
        Label(ventana, font=('Purple Smile', 20), text="Telefono", bg="#FFFFFF").place(x=94.0,
                                                                                y=300.0)

        telefono = Entry(ventana, font=('Purple Smile', 20),
                        background="#007FFF", fg="white")
        telefono.place(x=94.0,
                    y=350.0,
                    width=262.0,
                    height=43.0)

        Label(ventana, font=('Purple Smile', 20), text="Correo", bg="#FFFFFF").place(x=94.0,
                                                                            y=400.0)

        correo = Entry(ventana, font=('Purple Smile', 20),
                    background="#007FFF", fg="white")
        correo.place(x=94.0,
                    y=450.0,
                    width=262.0,
                    height=43.0)

    ventana.resizable(False, False)
    ventana.mainloop()


def menu_principal_grafico_inicio_sesion():  # login
    ventana.geometry("450x491")
    ventana.configure(bg="#FFFFFF")
    ventana.title("Abdera Glovo")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    abdera_icono = PhotoImage(
        file=relative_to_assets("icono.png"))

    Label(
        ventana,
        image=abdera_icono
    ).place(x=75, y=30)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_registro.png"))

    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_principal_grafico_registro(valor_guardado.get()),
        relief="flat"
    ).place(x=94.0,
            y=388.0,
            width=262.0,
            height=43.0
            )

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_sesion.png"))

    boton_inicio_sesion = Button(image=button_image_2,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 bg="#FFFFFF",
                                 command=lambda: iniciar_sesion(
                                     usuario.get(), contraseña.get(), valor_guardado.get()),
                                 relief="flat"
                                 )
    boton_inicio_sesion.place(x=94.0,
                              y=338.0,
                              width=262.0,
                              height=43.0
                              )

    Label(ventana, font=('Purple Smile', 20),
          text="Usuario", bg="#FFFFFF").place(x=94.0,
                                              y=125.0)

    usuario = Entry(ventana, font=('Purple Smile', 20), background="#007FFF", fg="white")
    usuario.place(x=94.0,
                  y=170.0,
                  width=262.0,
                  height=43.0)

    Label(ventana, font=('Purple Smile', 20), text="Contraseña", bg="#FFFFFF").place(x=94.0,
                                                                               y=215.0)

    contraseña = Entry(ventana, font=('Purple Smile', 20),
                       background="#007FFF", fg="white", show="*")
    contraseña.place(x=94.0,
                     y=260.0,
                     width=262.0,
                     height=43.0)
    valor_guardado = BooleanVar()
    checkbox = Checkbutton(ventana, font=('Purple Smile', 10), bg="#FFFFFF", text='Iniciar sesión o registro como gerente',
                           variable=valor_guardado, onvalue=True, offvalue=False)
    checkbox.place(x=94.0,
                   y=305.0)

    ventana.resizable(False, False)
    ventana.mainloop()


def menu_usuario_grafico(usuario):  # usuario
    ventana.geometry("450x491")
    ventana.configure(bg="#FFFFFF")
    ventana.title("Menu Principal")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_pedido.png"))

    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_restaurantes(usuario),
        relief="flat"
    ).place(
        x=94.0,
        y=277.0,
        width=262.0,
        height=43.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_credito.png"))
    Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_añadir_saldo(usuario),
        relief="flat"
    ).place(
        x=94.0,
        y=224.0,
        width=262.0,
        height=43.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("boton_historial.png"))
    Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_historial(usuario, "historial", ""),
        relief="flat"
    ).place(
        x=94.0,
        y=171.0,
        width=262.0,
        height=43.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("boton_pedidos.png"))
    Button(
        image=button_image_4,
        borderwidth=0,
        bg="#FFFFFF",
        highlightthickness=0,
        command=lambda: menu_historial(usuario, "tramites", ""),
        relief="flat"
    ).place(
        x=94.0,
        y=360.0,
        width=262.0,
        height=43.0
    )

    Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
          background="#6aa84f", text=f"Bienvenido de nuevo, {usuario}..").place(x=80.0,
                                                                                y=60.0,
                                                                                width=300.0,
                                                                                height=43.0)

    ventana.resizable(False, False)
    ventana.mainloop()


def menu_historial_regresar(usuario, restaurante):
    if (not bool(restaurante)):
        menu_usuario_grafico(usuario)
    else:
        menu_pedidos(restaurante, usuario)


def menu_historial(usuario, tipo, restaurante):
    ventana.title("Historial")
    ventana.geometry("450x491")

    
    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_regresar.png"))

    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: [menu_historial_regresar(
            usuario, restaurante), lista.clear()],
        relief="flat"
    ).place(
        x=94.0,
        y=351.0,
        width=262.0,
        height=43.0
    )

    carrito = ""
    lista = []
    precio = 0

    if (tipo == "historial"):
        for mostrar in clases.cliente.historial_clientes[usuario]:
            lista.append(str(mostrar).replace("Producto", "\nProducto")+"\n")
    elif (tipo == "tramites"):
        for mostrar in clases.restaurante.pedidos_tramite:
            lista.append(mostrar)
    elif (tipo == "carrito"):
        precio_total = 0
        for num_lista in clases.cliente.lista_compra.keys():
            carrito += str(f"[+] {clases.cliente.lista_compra[num_lista]['producto']} - Precio: {clases.cliente.lista_compra[num_lista]['precio']} €\n")
            precio += precio_total + clases.cliente.lista_compra[num_lista]['precio']

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_ver_historial.png"))

    if (tipo == "carrito"):
        Label(text=carrito).place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    else:
        boton_dic = {}
        contador = 0
        if (len(lista) <= 0):
            Label(text="No se ha encontrado nada en el historial...").place(
                relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        else:
            for mostrar in lista:
                if (contador >= 5):
                    break

                boton_dic[contador] = {Button(
                    image=button_image_2,
                    borderwidth=0,
                    highlightthickness=0,
                    bg="#FFFFFF",
                    text=contador,
                    command=lambda posicion=contador: menu_historial_por_item(
                        usuario, lista, posicion, restaurante, tipo),
                    relief="flat"
                ).place(
                    x=94.0,
                    y=30.0 + (60 * contador))}

                contador = contador+1

    ventana.resizable(False, False)
    ventana.mainloop()


def menu_historial_por_item(usuario, lista, posicion, restaurante, tipo):
    ventana.title("Historial")
    ventana.geometry("450x491")
    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_regresar.png"))

    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: [menu_historial(usuario, tipo, restaurante)],
        relief="flat"
    ).place(
        x=94.0,
        y=351.0,
        width=262.0,
        height=43.0
    )

    Label(text=lista[posicion], font=('Purple Smile', 8)).place(
        relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    ventana.resizable(False, False)
    ventana.mainloop()


def menu_restaurantes(usuario):
    ventana.title("Restaurantes")
    ventana.geometry("450x300")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    button_image_1 = PhotoImage(file=relative_to_assets("boton_continuar.png"))

    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_pedidos(combo.get(), usuario),
        relief="flat"
    ).place(
        x=89.0,
        y=190.0,
        width=262.0,
        height=43.0
    )

    lista = []

    for restaurantes in clases.restaurante.restaurantes_lista.keys():
        lista.append(restaurantes)

    Label(ventana, text="Selecciona el restaurante",
          font=('Purple Smile', 20), bg="#FFFFFF").place(x=46, y=80)

    combo = ttk.Combobox(
        state="readonly",
        values=lista,
        font=('Purple Smile', 20)
    )
    combo.current(0)
    combo.place(x=72.0, y=130.0, width=300.0, height=50.0)

    ventana.resizable(False, False)
    ventana.mainloop()


def comprobar_cancelacion(suficiente, usuario):
    if (suficiente):
        menu_usuario_grafico(usuario)
    else:
        error_texto = Label(ventana, font=('Purple Smile', 15), fg="#ffffff",
                            background="#dc3e3e", text="Error, no tienes suficiente saldo").place(x=80.0,
                                                                                              y=60.0,
                                                                                              width=300.0,
                                                                                              height=43.0)


def menu_pedidos(restaurante, usuario):
    ventana.title(f"Pedidos {restaurante}")
    ventana.geometry("450x491")
    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    abdera_icono = PhotoImage(
        file=relative_to_assets("icono.png"))

    Label(
        ventana,
        image=abdera_icono
    ).place(x=75, y=30)

    button_ver_carrito = PhotoImage(
        file=relative_to_assets("boton_carrito.png"))

    Button(
        image=button_ver_carrito,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_historial(usuario, "carrito", restaurante),
        relief="flat"
    ).place(
        x=94.0,
        y=134.0,
        width=262.0,
        height=43.0
    )

    button_image_2 = PhotoImage(file=relative_to_assets("boton_comidas.png"))

    Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_categoria(usuario, restaurante, "comidas"),
        relief="flat"
    ).place(
        x=94.0,
        y=186.0,
        width=262.0,
        height=43.0
    )

    button_image_3 = PhotoImage(file=relative_to_assets("boton_bebidas.png"))

    Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_categoria(usuario, restaurante, "bebidas"),
        relief="flat"
    ).place(
        x=94.0,
        y=239.0,
        width=262.0,
        height=43.0
    )

    button_image_4 = PhotoImage(file=relative_to_assets("boton_postres.png"))

    Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_categoria(usuario, restaurante, "postres"),
        relief="flat"
    ).place(
        x=94.0,
        y=292.0,
        width=262.0,
        height=43.0
    )

    button_image_5 = PhotoImage(file=relative_to_assets("boton_completar.png"))

    Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: [
            comprobar_cancelacion(clases.restaurante.Restaurante.aceptar_pedido(restaurante, usuario, True), usuario)],
        relief="flat"
    ).place(x=94.0,
            y=374.0,
            width=262.0,
            height=43.0
            )

    button_image_1 = PhotoImage(file=relative_to_assets("boton_cancelar.png"))

    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: [menu_usuario_grafico(
            usuario), clases.cliente.lista_compra.clear()],
        relief="flat"
    ).place(x=94.0, y=426.0, width=262.0, height=43.0)

    ventana.resizable(False, False)
    ventana.mainloop()


def iniciar_sesion(usuario, password, gerente):
    if (gerente):
        if (base_de_datos.database.Gerentes.comprobacion_gerente_sesion(usuario, password)):
            print("si")
        else:
            Label(ventana, font=('Purple Smile', 15), fg="#ffffff",
                                background="#dc3e3e", text="Error, Datos incorrectos").place(x=80.0,
                                                                                         y=60.0,
                                                                                         width=300.0,
                                                                                         height=43.0)
    else:
        if (base_de_datos.database.Usuarios.comprobacion_usuario_sesion(usuario, password)):
            
            Label(ventana, font=('Purple Smile', 15), fg="#ffffff",
                                        background="#6aa84f", text="Iniciando sesión en 5 segundos....").place(x=80.0,
                                                                                                                    y=60.0,
                                                                                                                    width=300.0,
                                                                                                                    height=43.0)
            
            menu_usuario_grafico(usuario) # Milliseconds and then a function
        else:
            Label(ventana, font=('Purple Smile', 15), fg="#ffffff",
                                background="#dc3e3e", text="Error, Datos incorrectos").place(x=80.0,
                                                                                         y=60.0,
                                                                                         width=300.0,
                                                                                         height=43.0)


def menu_añadir_saldo(usuario):  # usuario
    ventana.geometry("450x300")
    ventana.configure(bg="#FFFFFF")
    ventana.title("Añadir Saldo")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("boton_regresar.png"))
    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: menu_usuario_grafico(usuario),
        relief="flat"
    ).place(
        x=94.0,
        y=208.0,
        width=262.0,
        height=43.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("boton_continuar.png"))

    saldo_texto = Label(ventana, font=('Purple Smile', 15),
                        text=f"Saldo: {clases.cliente.Cliente.saldo(usuario)} €", bg="#FFFFFF")
    saldo_texto.place(x=94.0, y=50.0)

    def actualizar():    
        saldo_texto.config(text = f"Saldo: {clases.cliente.Cliente.saldo(usuario)} €")

    def completado_widget():
        Label(ventana, font=('Purple Smile', 20), fg="#ffffff",
              background="#6aa84f", text=f"Se ha añadido el saldo...").place(x=60.0,
                                                                             y=10.0)

    Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: [clases.cliente.Cliente.ingreso(usuario, float(saldo.get())), completado_widget(), actualizar()],
        relief="flat"
    ).place(
        x=94.0,
        y=158.0,
        width=262.0,
        height=43.0
    )

    saldo = Entry(ventana, font=('Purple Smile', 20), background="#007FFF", fg="white")
    saldo.place(x=94.0,
                y=90.0,
                width=262.0,
                height=43.0)
        

    ventana.resizable(False, False)
    ventana.mainloop()


def menu_categoria(usuario, nombre_restaurante, categoria):
    ventana.title("Categoria selección")

    canvas = Canvas(
        ventana,
        bg="#FFFFFF",
        height=491,
        width=450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    ).place(x=0, y=0)

    button_image_1 = PhotoImage(file=relative_to_assets("boton_añadir.png"))
    cantidad_arreglar = 0
    Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        bg="#FFFFFF",
        command=lambda: [clases.cliente.Cliente.pedido_añadir(nombre_restaurante, guardar_id, categoria, int(
            cantidad_arreglar)), menu_pedidos(nombre_restaurante, usuario)],
        relief="flat"
    ).place(
        x=94.0,
        y=351.0,
        width=262.0,
        height=43.0
    )

    lista = {}
    dictionary_a_lista = []
    contador = 0

    for menu in clases.restaurante.restaurantes_lista[nombre_restaurante][categoria]:
        lista[contador] = {f"{menu['nombre']} - Precio: {menu['precio']} €"}
        dictionary_a_lista.append(
            f"{menu['nombre']} - Precio: {menu['precio']} €")
        contador = contador+1

    Label(ventana, font=('Purple Smile', 18), text="Producto",
          bg="#FFFFFF").place(x=94.0, y=120.0)

    combo = ttk.Combobox(
        state="readonly",
        values=dictionary_a_lista,
        font=('Purple Smile', 20)
    )
    combo.current(0)
    combo.place(x=94.0, y=165.0)

    guardar_id = 0
    for name, values in lista.items():
        if values == combo.get():
            guardar_id = int(name)

    Label(ventana, font=('Purple Smile', 18),
          text="Cantidad", bg="#FFFFFF").place(x=94.0,
                                               y=215.0)

    cantidad = Entry(ventana, font=('Purple Smile', 20),
                     background="#007FFF", fg="white")
    cantidad.place(x=94.0, y=260.0)

    if (not cantidad.get() or int(cantidad.get()) < 0):
        cantidad_arreglar = 1
    else:
        cantidad_arreglar = cantidad.get()

    ventana.resizable(False, False)
    ventana.mainloop()
