def buscar_valor(matriz, valor):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, None

def main():
    matriz_ejemplo = [
        [1, 2, 3],
        [1, 5, 6],
        [7, 8, 9]
    ]

    valor_a_buscar = 5

    encontrado, posicion = buscar_valor(matriz_ejemplo, valor_a_buscar)

    if encontrado:
        print(f"El valor {valor_a_buscar} se encontro en la pocision {posicion}")

    else:
        print(f"El valor {valor_a_buscar} mo se encontro en la matriz")

if __name__ == "__main__":
    main()