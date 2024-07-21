# Archivo: pelicula.py

class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} ({self.genero}) - {self.duracion} min"



# Archivo: sala_cine.py

class SalaCine:
    def __init__(self, numero, capacidad, pelicula):
        self.numero = numero
        self.capacidad = capacidad
        self.pelicula = pelicula
        self.asientos_disponibles = capacidad

    def mostrar_info(self):
        return f"Sala {self.numero}: {self.pelicula} ({self.asientos_disponibles} asientos disponibles)"

    def reservar_asientos(self, cantidad):
        if cantidad <= self.asientos_disponibles:
            self.asientos_disponibles -= cantidad
            return True
        else:
            return False



# Archivo: main.py



# Crear instancias de películas
pelicula1 = Pelicula("Inception", 148, "Sci-Fi")
pelicula2 = Pelicula("The Dark Knight", 152, "Action")

# Crear instancias de salas de cine
sala1 = SalaCine(1, 100, pelicula1)
sala2 = SalaCine(2, 80, pelicula2)

# Mostrar información de las salas
print(sala1.mostrar_info())
print(sala2.mostrar_info())

# Reservar asientos
reserva1 = sala1.reservar_asientos(2)
reserva2 = sala2.reservar_asientos(3)

# Mostrar información actualizada de las salas después de las reservas
print(sala1.mostrar_info())
print(sala2.mostrar_info())

# Intentar reservar más asientos de los disponibles en sala1
reserva3 = sala1.reservar_asientos(99)
print("Reserva exitosa:", reserva1)  # True
print("Reserva exitosa:", reserva2)  # True
print("Reserva exitosa:", reserva3)  # False

