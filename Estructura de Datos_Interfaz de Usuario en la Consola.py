class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if self.buscar_por_id(producto.get_id()) is None:
            self.productos.append(producto)
            print(f"Producto {producto.get_nombre()} añadido.")
        else:
            print(f"El ID {producto.get_id()} ya existe en el inventario.")

    def eliminar_producto(self, id):
        producto = self.buscar_por_id(id)
        if producto:
            self.productos.remove(producto)
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"Producto con ID {id} no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = self.buscar_por_id(id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {id} actualizado.")
        else:
            print(f"Producto con ID {id} no encontrado.")

    def buscar_por_id(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                return producto
        return None

    def buscar_por_nombre(self, nombre):
        encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return encontrados

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n=== Sistema de Gestión de Inventario ===")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("Introduce el ID del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            cantidad = int(input("Introduce la cantidad: "))
            precio = float(input("Introduce el precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("Introduce el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Introduce el ID del producto a actualizar: ")
            cantidad = input("Introduce la nueva cantidad (dejar en blanco si no deseas cambiarla): ")
            precio = input("Introduce el nuevo precio (dejar en blanco si no deseas cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a buscar: ")
            productos = inventario.buscar_por_nombre(nombre)
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
