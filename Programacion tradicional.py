def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para el dia {i+1}"))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un numero valido")
    return temperaturas

def calculas_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)

#Fumcion principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calculas_promedio_semanal(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()