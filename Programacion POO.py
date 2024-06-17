class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el día {i + 1}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio_semanal(self):
        if not self.temperaturas:
            raise ValueError("No hay temperaturas ingresadas.")
        return sum(self.temperaturas) / len(self.temperaturas)


# Clase derivada que podría añadir más funcionalidades (herencia)
class ClimaExtendido(ClimaDiario):
    def __init__(self):
        super().__init__()
        self.humedad = []

    def ingresar_humedad(self):
        for i in range(7):
            while True:
                try:
                    humedad = float(input(f"Ingrese la humedad para el día {i + 1}: "))
                    self.humedad.append(humedad)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio_humedad(self):
        if not self.humedad:
            raise ValueError("No hay humedades ingresadas.")
        return sum(self.humedad) / len(self.humedad)


# Función principal
def main():
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio_temperatura = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de temperaturas es: {promedio_temperatura:.2f}°C")

    clima_extendido = ClimaExtendido()
    clima_extendido.ingresar_temperaturas()
    clima_extendido.ingresar_humedad()
    promedio_temperatura_extendido = clima_extendido.calcular_promedio_semanal()
    promedio_humedad = clima_extendido.calcular_promedio_humedad()
    print(f"El promedio semanal de temperaturas (extendido) es: {promedio_temperatura_extendido:.2f}°C")
    print(f"El promedio semanal de humedad es: {promedio_humedad:.2f}%")


if __name__ == "__main__":
    main()
