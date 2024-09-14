# Clase Libro: Representa un libro con atributos inmutables (título y autor) y mutables (categoría, ISBN).
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo={self.info[0]}, autor={self.info[1]}, categoria={self.categoria}, ISBN={self.isbn})"


# Clase Usuario: Representa un usuario con un ID único y una lista de libros actualmente prestados.
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para libros prestados

    def __repr__(self):
        return f"Usuario(nombre={self.nombre}, ID={self.id_usuario}, libros_prestados={self.libros_prestados})"


# Clase Biblioteca: Gestiona los libros, usuarios y préstamos.
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios_registrados = set()  # Conjunto para asegurar IDs únicos de usuarios
        self.historial_prestamos = {}  # Diccionario para mantener el historial de préstamos de cada usuario

    # Añadir libro a la biblioteca
    def anadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    # Quitar libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro '{libro.info[0]}' removido de la biblioteca.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn} en la biblioteca.")

    # Registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.historial_prestamos[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    # Dar de baja un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.historial_prestamos.pop(id_usuario)
            self.usuarios_registrados.remove(id_usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print(f"No se encontró ningún usuario con ID {id_usuario}.")

    # Prestar libro a un usuario
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.historial_prestamos[id_usuario]
            if isbn in self.libros_disponibles:
                libro = self.libros_disponibles.pop(isbn)
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
            else:
                print(f"El libro con ISBN {isbn} no está disponible.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.historial_prestamos[id_usuario]
            libro_devolver = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
            if libro_devolver:
                usuario.libros_prestados.remove(libro_devolver)
                self.libros_disponibles[isbn] = libro_devolver
                print(f"Libro '{libro_devolver.info[0]}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    # Buscar libro por título, autor o categoría
    def buscar_libro(self, filtro, tipo_busqueda="titulo"):
        libros_encontrados = []
        for libro in self.libros_disponibles.values():
            if tipo_busqueda == "titulo" and filtro.lower() in libro.info[0].lower():
                libros_encontrados.append(libro)
            elif tipo_busqueda == "autor" and filtro.lower() in libro.info[1].lower():
                libros_encontrados.append(libro)
            elif tipo_busqueda == "categoria" and filtro.lower() in libro.categoria.lower():
                libros_encontrados.append(libro)

        if libros_encontrados:
            print(f"Libros encontrados para '{filtro}' ({tipo_busqueda}):")
            for libro in libros_encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con el {tipo_busqueda} '{filtro}'.")

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.historial_prestamos[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")


# Función principal con un menú interactivo
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Menú Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados a un usuario")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Añadir libro
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.anadir_libro(libro)

        elif opcion == "2":
            # Quitar libro
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Registrar usuario
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            # Dar de baja usuario
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            # Prestar libro
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            # Devolver libro
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            # Buscar libro
            tipo_busqueda = input("Buscar por (titulo/autor/categoria): ").lower()
            filtro = input(f"Introduce el {tipo_busqueda} del libro: ")
            biblioteca.buscar_libro(filtro, tipo_busqueda)

        elif opcion == "8":
            # Listar libros prestados a un usuario
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            print("Saliendo del sistema de biblioteca...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejecutar el menú interactivo
if __name__ == "__main__":
    menu()
