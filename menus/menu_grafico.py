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


class Registro_Inicio_Sesion():
    def iniciar_sesion(usuario, password, gerente):
        if (gerente):
            if (base_de_datos.database.Gerentes.comprobacion_gerente_sesion(usuario, password)):

                Label(ventana, font=('Purple Smile', 13), fg="#ffffff",
                      background="#6aa84f", text="Iniciando sesion en 5 segundos...").place(x=80.0,
                                                                                             y=60.0,
                                                                                             width=300.0,
                                                                                             height=43.0)

                ventana.after(5000, lambda : [ Menu_Restaurante.menu_restaurante_grafico(usuario) ]) 

            else:
                Label(ventana, font=('Purple Smile', 15), fg="#ffffff",
                      background="#dc3e3e", text="Error, Datos incorrectos").place(x=80.0,
                                                                                   y=60.0,
                                                                                   width=300.0,
                                                                                   height=43.0)
        else:
            if (base_de_datos.database.Usuarios.comprobacion_usuario_sesion(usuario, password)):

                Label(ventana, font=('Purple Smile', 13), fg="#ffffff",
                      background="#6aa84f", text="Iniciando sesion en 5 segundos...").place(x=80.0,
                                                                                             y=60.0,
                                                                                             width=300.0,
                                                                                             height=43.0)

                ventana.after(5000, lambda : [ Menu_Usuario.menu_usuario_grafico(usuario) ]) 
            else:
                Label(ventana, font=('Purple Smile', 15), fg="#ffffff",
                      background="#dc3e3e", text="Error, Datos incorrectos").place(x=80.0,
                                                                                   y=60.0,
                                                                                   width=300.0,
                                                                                   height=43.0)

    def registrar_funcion(nombre, password, telefono, correo, gerente):
                if (gerente):
                    if(not nombre or not password):
                        Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                            background="#dc3e3e", text="Error, los campos se encuentran vacios...").place(x=30.0,
                                                                                                            y=30.0,
                                                                                                            width=400.0,
                                                                                                            height=43.0)
                    elif (base_de_datos.database.Gerentes.existe_restaurante(nombre)):
                        error_texto = Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                                            background="#dc3e3e", text="Error, el nombre ya se encuentra registrado...").place(x=30.0,
                                                                                                                               y=30.0,
                                                                                                                               width=400.0,
                                                                                                                               height=43.0)
                    else:
                        registrar = clases.restaurante.Restaurante(
                            nombre, password, "", "", "", 0)

                        clases.restaurante.restaurantes_lista[nombre] = {
                            "bebidas": [{ "nombre": "agua", "precio": 1.0 }],
                            "comidas": [{ "nombre": "pollo", "precio": 3.0 }],
                            "postres": [{ "nombre": "tarta", "precio": 2.50 }],
                            "reputacion": 0,
                            "password": password}  # esto para el dictionario

                        # registramos los nuevos valores a la clase
                        clases.restaurante.restaurantes_clase.append(registrar)

                        base_de_datos.database.Gerentes.añadir_datos(
                            clases.restaurante.restaurantes_lista)  # añadimos los nuevos valores al json
                        Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                              background="#6aa84f", text="Se ha completado, en 5 sera redirigido segundos....").place(x=30.0,
                                                                                                      y=30.0,
                                                                                                      width=400.0,
                                                                                                      height=43.0)
                        ventana.after(5000, lambda : [ Registro_Inicio_Sesion.menu_principal_grafico_inicio_sesion() ])                 
                else:
                    if(not nombre or not password or not telefono or not correo):
                        Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                            background="#dc3e3e", text="Error, los campos se encuentran vacios...").place(x=30.0,
                                                                                                            y=30.0,
                                                                                                            width=400.0,
                                                                                                            height=43.0)
                    elif(not funciones.funciones.email_es_valido(correo)):
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

                            Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
                              background="#6aa84f", text="Se ha completado, en 5 sera redirigido segundos....").place(x=30.0,
                                                                                                      y=30.0,
                                                                                                      width=300.0,
                                                                                                      height=43.0)
                            ventana.after(5000, lambda : [ Registro_Inicio_Sesion.menu_principal_grafico_inicio_sesion() ])  

    def menu_principal_grafico_registro(gerente):  # registro
        ventana.geometry(f"450x{'460' if gerente else '640'}")
        ventana.configure(bg="#FFFFFF")
        ventana.title("Registro")

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
            command=lambda: Registro_Inicio_Sesion.registrar_funcion(usuario.get(), contraseña.get(
            ), "" if gerente else telefono.get(), "" if gerente else correo.get(), gerente),
            relief="flat"
        ).place(x=94.0,
                y=325 if gerente else 520,
                width=262.0,
                height=43.0
                )
        
        button_image_2 = PhotoImage(
            file=relative_to_assets("boton_atras.png"))

        Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Registro_Inicio_Sesion.menu_principal_grafico_inicio_sesion(),
            relief="flat"
        ).place(x=94.0,
                y=375 if gerente else 570,
                width=262.0,
                height=43.0
                )

        Label(ventana, font=('Purple Smile', 20),
              text="Usuario", bg="#FFFFFF").place(x=94.0,
                                                  y=100.0)

        usuario = Entry(ventana, font=('Purple Smile', 20),
                        background="#007FFF", fg="white")
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
            command=lambda: Registro_Inicio_Sesion.menu_principal_grafico_registro(
                valor_guardado.get()),
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
                                     command=lambda: Registro_Inicio_Sesion.iniciar_sesion(
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

        usuario = Entry(ventana, font=('Purple Smile', 20),
                        background="#007FFF", fg="white")
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


class Menu_Usuario():
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
            command=lambda: Menu_Usuario.menu_restaurantes(usuario),
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
            command=lambda: Menu_Usuario.menu_añadir_saldo(usuario),
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
            command=lambda: Menu_Usuario.menu_historial(
                usuario, "historial", "", 1),
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
            command=lambda: Menu_Usuario.menu_historial(
                usuario, "tramites", "", 1),
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
            Menu_Usuario.menu_usuario_grafico(usuario)
        else:
            Menu_Usuario.menu_pedidos(restaurante, usuario)

    def menu_historial(usuario, tipo, restaurante, pagina):
        ventana.geometry("450x510")

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
            command=lambda: [Menu_Usuario.menu_historial_regresar(
                usuario, restaurante), lista.clear()],
            relief="flat"
        ).place(
            x=94.0,
            y=351.0,
            width=262.0,
            height=43.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("boton_siguiente.png"))

        boton_dic = {}
        carrito = ""
        lista = []
        precio = 0
        if (tipo != "carrito"):
            Button(
                image=button_image_3,
                borderwidth=0,
                highlightthickness=0,
                bg="#FFFFFF",
                command=lambda: [siguiente_funcion()],
                relief="flat"
            ).place(
                x=94.0,
                y=400.0,
                width=262.0,
                height=43.0
            )

            button_image_4 = PhotoImage(
                file=relative_to_assets("boton_atras.png"))

            Button(
                image=button_image_4,
                borderwidth=0,
                highlightthickness=0,
                bg="#FFFFFF",
                command=lambda: [atras_funcion()],
                relief="flat"
            ).place(
                x=94.0,
                y=449.0,
                width=262.0,
                height=43.0
            )

        if (tipo == "historial"):
            for mostrar in clases.cliente.historial_clientes[usuario]:
                lista.append(str(mostrar).replace(
                    "Producto", "\nProducto")+"\n")
        elif (tipo == "tramites"):
            lista = clases.restaurante.pedidos_tramite
        elif (tipo == "carrito"):
            precio_total = 0
            for num_lista in clases.cliente.lista_compra.keys():
                carrito += str(f"[+] {clases.cliente.lista_compra[num_lista]['producto']} - Precio: {clases.cliente.lista_compra[num_lista]['precio']} €\n")
                precio += precio_total + \
                    clases.cliente.lista_compra[num_lista]['precio']

        button_image_2 = PhotoImage(
            file=relative_to_assets("boton_ver_historial.png"))

        item_por_pagina = 5
        total_paginas = len(lista) // item_por_pagina + 1  # Total de páginas
        pagina_actual = StringVar()

        def siguiente_funcion():
            boton_dic.clear()
            current_page = int(pagina_actual.get().split()[1])
            if current_page < total_paginas:
                Menu_Usuario.menu_historial(
                    usuario, tipo, restaurante, current_page + 1)

        def mostrar_pagina(pagina_num):
            contador = 0
            primer_index = (pagina_num - 1) * item_por_pagina
            ultimo_index = primer_index + item_por_pagina
            items_de_la_pagina = lista[primer_index:ultimo_index]
            pagina_actual.set("Página {} de {}".format(
                pagina_num, total_paginas))
            for items in items_de_la_pagina:
                boton_dic[contador] = {Button(
                    image=button_image_2,
                    borderwidth=0,
                    highlightthickness=0,
                    bg="#FFFFFF",
                    text=contador,
                    command=lambda texto=items: Menu_Usuario.menu_historial_por_item(
                        usuario, restaurante, tipo, texto, pagina_num),
                    relief="flat"
                ).place(
                    x=94.0,
                    y=30.0 + (60 * contador))}
                contador = contador+1

        def atras_funcion():
            current_page = int(pagina_actual.get().split()[1])
            if current_page > 1:
                Menu_Usuario.menu_historial(
                    usuario, tipo, restaurante, current_page - 1)

        if (tipo == "carrito"):
            Label(text=carrito).place(
                relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        else:
            if (len(lista) <= 0):
                Label(text="No se ha encontrado nada en el historial...", font=('Purple Smile', 10), fg="#ffffff").place(
                    relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            else:
                mostrar_pagina(pagina)

        page_label = Label(ventana, textvariable=pagina_actual,
                           font=('Purple Smile', 10))
        page_label.place(
            x=178.0,
            y=4.0)

        ventana.resizable(False, False)
        ventana.mainloop()

    def menu_historial_por_item(usuario, restaurante, tipo, texto, pagina):
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
            command=lambda: [Menu_Usuario.menu_historial(
                usuario, tipo, restaurante, pagina)],
            relief="flat"
        ).place(
            x=94.0,
            y=351.0,
            width=262.0,
            height=43.0
        )

        Label(text=texto, font=('Purple Smile', 8)).place(
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

        button_image_1 = PhotoImage(
            file=relative_to_assets("boton_continuar.png"))

        Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Usuario.menu_pedidos(combo.get(), usuario),
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
            Menu_Usuario.menu_usuario_grafico(usuario)
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
            image=abdera_icono,
            fg="#ffffff"
        ).place(x=75, y=30)

        button_ver_carrito = PhotoImage(
            file=relative_to_assets("boton_carrito.png"))

        Button(
            image=button_ver_carrito,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Usuario.menu_historial(
                usuario, "carrito", restaurante, 1),
            relief="flat"
        ).place(
            x=94.0,
            y=134.0,
            width=262.0,
            height=43.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("boton_comidas.png"))

        Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Usuario.menu_categoria(
                usuario, restaurante, "comidas"),
            relief="flat"
        ).place(
            x=94.0,
            y=186.0,
            width=262.0,
            height=43.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("boton_bebidas.png"))

        Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Usuario.menu_categoria(
                usuario, restaurante, "bebidas"),
            relief="flat"
        ).place(
            x=94.0,
            y=239.0,
            width=262.0,
            height=43.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("boton_postres.png"))

        Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Usuario.menu_categoria(
                usuario, restaurante, "postres"),
            relief="flat"
        ).place(
            x=94.0,
            y=292.0,
            width=262.0,
            height=43.0
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("boton_completar.png"))

        Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [
                Menu_Usuario.comprobar_cancelacion(clases.restaurante.Restaurante.aceptar_pedido(restaurante, usuario, True), usuario)],
            relief="flat"
        ).place(x=94.0,
                y=374.0,
                width=262.0,
                height=43.0
                )

        button_image_1 = PhotoImage(
            file=relative_to_assets("boton_cancelar.png"))

        Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [Menu_Usuario.menu_usuario_grafico(
                usuario), clases.cliente.lista_compra.clear()],
            relief="flat"
        ).place(x=94.0, y=426.0, width=262.0, height=43.0)

        ventana.resizable(False, False)
        ventana.mainloop()

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
            command=lambda: Menu_Usuario.menu_usuario_grafico(usuario),
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
            saldo_texto.config(
                text=f"Saldo: {clases.cliente.Cliente.saldo(usuario)} €")

        def completado_widget():
            Label(ventana, font=('Purple Smile', 20), fg="#ffffff",
                  background="#6aa84f", text=f"Se ha añadido el saldo...").place(x=60.0,
                                                                                 y=10.0)

        Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [clases.cliente.Cliente.ingreso(
                usuario, float(saldo.get())), completado_widget(), actualizar()],
            relief="flat"
        ).place(
            x=94.0,
            y=158.0,
            width=262.0,
            height=43.0
        )

        saldo = Entry(ventana, font=('Purple Smile', 20),
                      background="#007FFF", fg="white")
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

        button_image_1 = PhotoImage(
            file=relative_to_assets("boton_añadir.png"))

        Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [clases.cliente.Cliente.pedido_añadir(nombre_restaurante, guardar_id, categoria, int(
                cantidad.get())), Menu_Usuario.menu_pedidos(nombre_restaurante, usuario)],
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
            lista[contador] = {
                f"{menu['nombre']} - Precio: {menu['precio']} €"}
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

        ventana.resizable(False, False)
        ventana.mainloop()


class Menu_Restaurante():        
    def obtener_id(valor_buscar, diccionario):
        guardar_id = 0
        for name, values in diccionario.items():
            if values == valor_buscar:
                return int(name)

        return guardar_id
    
    def seleccion(restaurante, categoria, remover):
        ventana.title(f"Menu de {restaurante}")
        ventana.geometry(f"450x{'300' if remover else '455'}")
        canvas = Canvas(
            ventana,
            bg="#FFFFFF",
            height=491,
            width=450,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        ).place(x=0, y=0)

        dictionary_a_lista = []
        diccionario = {}
        contador=0

        for menu in clases.restaurante.restaurantes_lista[restaurante][categoria]:
            dictionary_a_lista.append(f"{menu['nombre']} - Precio: {menu['precio']} €")
            diccionario[contador] = f"{menu['nombre']} - Precio: {menu['precio']} €"
            contador=contador+1

        Label(ventana, text=f"{'Selecciona el menu' if remover else 'Menu lista'}",
              font=('Purple Smile', 20), bg="#FFFFFF").place(x=94, y=10)

        combo = ttk.Combobox(
            state="readonly",
            values=dictionary_a_lista,
            font=('Purple Smile', 20)
        )
        combo.current(0)
        combo.place(x=94.0, y=50.0, width=300.0, height=50.0)

        if(not remover):
            Label(ventana, font=('Purple Smile', 20), text="Nombre", bg="#FFFFFF").place(x=94.0,
                                                                                         y=100.0)
            
            nombre_producto = Entry(ventana, font=('Purple Smile', 20),
                            background="#007FFF", fg="white")
            nombre_producto.place(x=94.0,
                            y=150.0,
                            width=262.0,
                            height=43.0)
            
            Label(ventana, font=('Purple Smile', 20), text="Precio", bg="#FFFFFF").place(x=94.0,
                                                                                            y=200.0)

            precio_producto = Entry(ventana, font=('Purple Smile', 20),
                            background="#007FFF", fg="white")
            precio_producto.place(x=94.0,
                            y=250.0,
                            width=262.0,
                            height=43.0)
            
            button_image_2 = PhotoImage(
                file=relative_to_assets("boton_añadir.png"))

            Button(
                image=button_image_2,
                borderwidth=0,
                highlightthickness=0,
                bg="#FFFFFF",
                command=lambda: [base_de_datos.database.Gerentes.añadir_producto(restaurante, categoria, nombre_producto.get(), float(precio_producto.get())), dictionary_a_lista.clear(), diccionario.clear(), Menu_Restaurante.menu_pedidos(
                restaurante)],
                relief="flat"
            ).place(x=94.0, y=300.0, width=262.0, height=43.0)
        else:    
            button_image_3 = PhotoImage(
            file=relative_to_assets("boton_remover.png"))

            Button(
                image=button_image_3,
                borderwidth=0,
                highlightthickness=0,
                bg="#FFFFFF",
                command=lambda: [base_de_datos.database.Gerentes.remover_producto(Menu_Restaurante.obtener_id(combo.get(), diccionario), restaurante, categoria), dictionary_a_lista.clear(), diccionario.clear(), Menu_Restaurante.menu_pedidos(
                restaurante)],
                relief="flat"
            ).place(x=94.0, y=150, width=262.0, height=43.0)

        button_image_1 = PhotoImage(
            file=relative_to_assets("boton_regresar.png"))

        Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [Menu_Restaurante.menu_pedidos(
                restaurante), dictionary_a_lista.clear(), diccionario.clear()],
            relief="flat"
        ).place(x=94.0, y=200.0 if remover else 350, width=262.0, height=43.0)

        ventana.resizable(False, False)
        ventana.mainloop()

    def menu_pedidos(restaurante):
        ventana.title(f"Menu de {restaurante}")
        ventana.geometry("450x450")
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
            image=abdera_icono,
            fg="#ffffff"
        ).place(x=75, y=30)

        button_image_2 = PhotoImage(
            file=relative_to_assets("boton_comidas.png"))

        Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Restaurante.seleccion_modificar(restaurante, "comidas"),
            relief="flat"
        ).place(
            x=94.0,
            y=186.0,
            width=262.0,
            height=43.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("boton_bebidas.png"))

        Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Restaurante.seleccion_modificar(restaurante, "bebidas"),
            relief="flat"
        ).place(
            x=94.0,
            y=239.0,
            width=262.0,
            height=43.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("boton_postres.png"))

        Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Restaurante.seleccion_modificar(restaurante, "postres"),
            relief="flat"
        ).place(
            x=94.0,
            y=292.0,
            width=262.0,
            height=43.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("boton_regresar.png"))

        Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [Menu_Restaurante.menu_restaurante_grafico(
                restaurante)],
            relief="flat"
        ).place(x=94.0, y=347.0, width=262.0, height=43.0)

        ventana.resizable(False, False)
        ventana.mainloop()

    def seleccion_modificar(restaurante, categoria):
        ventana.geometry("450x200")
        ventana.configure(bg="#FFFFFF")
        ventana.title("Modificar menu")

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
            file=relative_to_assets("boton_añadir.png"))

        Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Restaurante.seleccion(restaurante, categoria, False),
            relief="flat"
        ).place(
            x=94.0,
            y=50.0,
            width=262.0,
            height=43.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("boton_remover.png"))
        Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Restaurante.seleccion(restaurante, categoria, True),
            relief="flat"
        ).place(
            x=94.0,
            y=100.0,
            width=262.0,
            height=43.0
        )

        ventana.resizable(False, False)
        ventana.mainloop()

    def menu_regresar_seguir(restaurante, volver, pagina):
        if(volver):
            Menu_Restaurante.menu_restaurante_grafico(restaurante)
        else:
            Menu_Restaurante.menu_historial(restaurante, pagina)

    def menu_historial(restaurante, pagina):
        ventana.geometry("450x510")

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
            command=lambda: [Menu_Restaurante.menu_regresar_seguir(restaurante, True, pagina), lista.clear()],
            relief="flat"
        ).place(
            x=94.0,
            y=351.0,
            width=262.0,
            height=43.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("boton_siguiente.png"))

        boton_dic = {}
        lista = []

        Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [siguiente_funcion()],
            relief="flat"
        ).place(
            x=94.0,
            y=400.0,
            width=262.0,
            height=43.0
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("boton_atras.png"))

        Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: [atras_funcion()],
            relief="flat"
        ).place(
            x=94.0,
            y=449.0,
            width=262.0,
            height=43.0
        )
        no_existe = False

        try:
            for mostrar in clases.restaurante.historial_restaurantes[restaurante]:
                lista.append(str(mostrar).replace("Producto", "\nProducto")+"\n")
        except:
            no_existe = True

        button_image_2 = PhotoImage(
            file=relative_to_assets("boton_ver_historial.png"))

        item_por_pagina = 5
        total_paginas = len(lista) // item_por_pagina + 1  # Total de páginas
        pagina_actual = StringVar()

        def siguiente_funcion():
            boton_dic.clear()
            current_page = int(pagina_actual.get().split()[1])
            if current_page < total_paginas:
                Menu_Restaurante.menu_historial(restaurante, current_page + 1)

        def mostrar_pagina(pagina_num):
            contador = 0
            primer_index = (pagina_num - 1) * item_por_pagina
            ultimo_index = primer_index + item_por_pagina
            items_de_la_pagina = lista[primer_index:ultimo_index]
            pagina_actual.set("Página {} de {}".format(
                pagina_num, total_paginas))
            for items in items_de_la_pagina:
                boton_dic[contador] = {Button(
                    image=button_image_2,
                    borderwidth=0,
                    highlightthickness=0,
                    bg="#FFFFFF",
                    text=contador,
                    command=lambda texto=items: Menu_Restaurante.menu_historial_por_item(
                        restaurante, texto, pagina_num),
                    relief="flat"
                ).place(
                    x=94.0,
                    y=30.0 + (60 * contador))}
                contador = contador+1

        def atras_funcion():
            current_page = int(pagina_actual.get().split()[1])
            if current_page > 1:
                Menu_Restaurante.menu_historial(restaurante, current_page - 1)

        if (len(lista) <= 0 and no_existe):
            Label(text="No se ha encontrado nada en el historial...", font=(
                'Purple Smile', 10), fg="#ffffff").place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        else:
            mostrar_pagina(pagina)

        page_label = Label(ventana, textvariable=pagina_actual,
                           font=('Purple Smile', 10))
        page_label.place(
            x=178.0,
            y=4.0)

        ventana.resizable(False, False)
        ventana.mainloop()

    def menu_historial_por_item(restaurante, texto, pagina):
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
            command=lambda: [
                Menu_Restaurante.menu_regresar_seguir(restaurante, False, pagina)],
            relief="flat"
        ).place(
            x=94.0,
            y=351.0,
            width=262.0,
            height=43.0
        )

        Label(text=texto, font=('Purple Smile', 8)).place(
            relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        ventana.resizable(False, False)
        ventana.mainloop()

    def menu_restaurante_grafico(usuario):  # usuario
        ventana.geometry("450x300")
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
            file=relative_to_assets("boton_menus.png"))

        Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            bg="#FFFFFF",
            command=lambda: Menu_Restaurante.menu_pedidos(usuario),
            relief="flat"
        ).place(
            x=94.0,
            y=124.0,
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
            command=lambda: Menu_Restaurante.menu_historial(
                usuario, 1),
            relief="flat"
        ).place(
            x=94.0,
            y=177.0,
            width=262.0,
            height=43.0
        )

        Label(ventana, font=('Purple Smile', 10), fg="#ffffff",
              background="#6aa84f", text=f"Bienvenido de nuevo, gerente {usuario}..").place(x=80.0,
                                                                                            y=60.0,
                                                                                            width=300.0,
                                                                                            height=43.0)

        ventana.resizable(False, False)
        ventana.mainloop()
