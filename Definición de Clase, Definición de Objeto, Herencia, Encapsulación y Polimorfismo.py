# Definición de la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca          # atributo público
        self.__modelo = modelo      # atributo privado

    def get_modelo(self):
        return self.__modelo       # método para acceder al atributo privado

    def conducir(self):
        raise NotImplementedError("Método conducir() no implementado en la clase base")

# Definición de la clase derivada Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def conducir(self):
        return f"El {self.marca} {self.get_modelo()} de color {self.color} está en movimiento."

    def __str__(self):
        return f"Automóvil {self.marca} {self.get_modelo()}, color {self.color}"

# Función principal para demostrar el programa
def main():
    # Crear instancia de Automovil
    automovil1 = Automovil("Toyota", 2023, "Rojo")

    # Acceder a métodos de la clase derivada
    print(automovil1.conducir())

    # Polimorfismo: utilizando el método __str__()
    print(str(automovil1))

if __name__ == "__main__":
    main()
