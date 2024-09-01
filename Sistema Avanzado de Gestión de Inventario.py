import json


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if p.get_nombre().lower() == nombre.lower()]

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            data = {id: vars(p) for id, p in self.productos.items()}
            json.dump(data, archivo)

    def cargar_de_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                data = json.load(archivo)
                self.productos = {id: Producto(**p) for id, p in data.items()}
        except FileNotFoundError:
            print("El archivo no existe.")


def mostrar_menu():
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar en archivo")
    print("7. Cargar desde archivo")
    print("8. Salir")


def main():
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id,
                                           cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_por_nombre(nombre)
            for producto in productos:
                print(producto)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            nombre_archivo = input("Nombre del archivo para guardar: ")
            inventario.guardar_en_archivo(nombre_archivo)

        elif opcion == "7":
            nombre_archivo = input("Nombre del archivo para cargar: ")
            inventario.cargar_de_archivo(nombre_archivo)

        elif opcion == "8":
            break


if __name__ == "__main__":
    main()
