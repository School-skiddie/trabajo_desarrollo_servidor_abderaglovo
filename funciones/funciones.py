import re, os, platform

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def email_es_valido(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False

def pausa():
    input("\nPresiona enter tecla para continuar...")

def borrar_pantalla():
    os.system(f"{'cls' if platform.system() == 'Windows' else 'clear'}")