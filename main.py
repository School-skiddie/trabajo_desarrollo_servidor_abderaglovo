import menus.menu, base_de_datos.database, menus.menu_grafico

grafico = True

base_de_datos.database.Usuarios.cargar_usuarios() # cargamos el json y lo pasamos a la clase con un for
base_de_datos.database.Usuarios.cargar_historial_usuarios()

base_de_datos.database.Gerentes.cargar_restaurantes()
base_de_datos.database.Gerentes.cargar_historial_restaurantes()

if(grafico):
    menus.menu_grafico.Registro_Inicio_Sesion.menu_principal_grafico_inicio_sesion()
else:
    menus.menu.menu_principal() # cargamos el menu