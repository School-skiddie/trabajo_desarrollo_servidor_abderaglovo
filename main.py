import menus.menu
import base_de_datos.database


# main


base_de_datos.database.cargar_usuarios() # cargamos el json y lo pasamos a la clase con un for
menus.menu.menu_principal() # cargamos el menu