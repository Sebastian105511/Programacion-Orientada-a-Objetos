class Archivo:
    def __init__(self, nombre):
        # Constructor: Se llama al crear una instancia de la clase
        self.nombre = nombre
        print(f"Creando el archivo: {self.nombre}")
        self.archivo = open(self.nombre, 'w')

    def escribir(self, texto):
        # Método para escribir en el archivo
        self.archivo.write(texto)
        print(f"Escribiendo en el archivo: {self.nombre}")

    def __del__(self):
        # Destructor: Se llama cuando el objeto es destruido
        if hasattr(self, 'archivo') and self.archivo:
            self.archivo.close()
            print(f"Cerrando el archivo: {self.nombre}")


# Uso de la clase
archivo1 = Archivo('ejemplo.txt')
archivo1.escribir('Hola, mundo!')

# El objeto archivo1 será destruido al finalizar el programa o cuando se llame explícitamente a del
del archivo1
