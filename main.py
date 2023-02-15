import menus.menu, base_de_datos.database

base_de_datos.database.cargar_usuarios() # cargamos el json y lo pasamos a la clase con un for
base_de_datos.database.cargar_historial_usuarios()
menus.menu.menu_principal() # cargamos el menu