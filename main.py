import menus.menu, base_de_datos.database, os, menus.menu_grafico


base_de_datos.database.Usuarios.cargar_usuarios() # cargamos el json y lo pasamos a la clase con un for
base_de_datos.database.Usuarios.cargar_historial_usuarios()

base_de_datos.database.Gerentes.cargar_restaurantes()
base_de_datos.database.Gerentes.cargar_historial_restaurantes()

menus.menu_grafico.menu_principal_grafico_inicio_sesion()
#menus.menu.menu_principal() # cargamos el menu