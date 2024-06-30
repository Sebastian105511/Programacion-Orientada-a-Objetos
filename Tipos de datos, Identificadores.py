#Este progama es para calcular el area de un circulo y un rectangulo.
#Utiliza diferentes tipos de datos y sigue las convenciones de estilo de Python.

def calcular_area_circulo(radio):
    """
    Calcula el area de un circulo dado su radio

    :param radio: El radio del circulo(float).
    :return: El area del circulo(float).
    """
    pi= 3.14159 # Definicion de pi como constante
    area = pi*radio**2 # Formula para el area del circulo
    return area

def calcular_area_rectangulo(base, altura):
    """
    Calcula el area de un rectangulo dada su basey altura

    :param base: La base del rectangulo (float).
    :param altura: La altura del rectangulo (float).
    :return: El area del rectangulo (float).
    """
    area = base * altura #Formula para el area del rectangulo
    return area

def main():
    """
    Funcion principal del programa. Solicita al usuario que ingrese los datos y muestra los resultados.
    """
    #Solicitar al usuario que ingrese el radio del circulo
    radio= float(input("Ingrese el radio del circulo: "))
    #Calcular y mostrar el area del circulo
    area_circulo = calcular_area_circulo(radio)
    print(f"El area del circulo con el radio {radio} es {area_circulo}")

    # Solicitar al usuario que ingrese la base y la altura del rectángulo
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    # Calcular y mostrar el área del rectángulo
    area_rectangulo = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo con base {base} y altura {altura} es {area_rectangulo}")

#Llamada al funcion principal.
if __name__ == "__main__":
    main()