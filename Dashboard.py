import os


def mostrar_codigo(ruta_script):
    """
    Muestra el contenido del archivo de script especificado.

    Args:
        ruta_script (str): La ruta al archivo de script.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def agregar_opcion(opciones):
    """
    Permite al usuario agregar una nueva opción de script al menú.

    Args:
        opciones (dict): Diccionario con las opciones actuales del menú.
    """
    nueva_clave = input("Introduce el número para la nueva opción: ")
    nueva_ruta = input("Introduce la ruta del nuevo script: ")
    if nueva_clave in opciones:
        print("Esa opción ya existe. Intenta de nuevo.")
    else:
        opciones[nueva_clave] = nueva_ruta
        print("Opción agregada con éxito.")


def mostrar_menu():
    """
    Muestra el menú principal y permite al usuario elegir qué script ver.
    """
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/1.2. Tecnicas de Programacion/1.2-1. Ejemplo Tecnicas de Programacion.py',
        # Agrega aquí el resto de las rutas de los scripts
        '2': 'Constructores y Destructores.py',
        '3': 'Programacion POO.py',
        '4': 'Tipos de datos, Identificadores.py',
        '5': 'Programacion tradicional.py',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("a - Agregar nueva opción")
        print("0 - Salir")
#Se agrego una opcion que al usario le permite agragar rutas de scrip
        eleccion = input("Elige un script para ver su código, 'a' para agregar una nueva opción o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion == 'a':
            agregar_opcion(opciones)
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
