def ordenar_fila(matriz, fila):

    if fila < 0 or fila >= len(matriz):
        print("Fila especificada no válida")
        return


    for i in range(len(matriz[fila])-1):
        for j in range(len(matriz[fila])-1-i):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiar elementos si están en el orden incorrecto
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():

    matriz_ejemplo = [
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ]


    print("Matriz original:")
    imprimir_matriz(matriz_ejemplo)


    fila_a_ordenar = 1
    ordenar_fila(matriz_ejemplo, fila_a_ordenar)


    print("\nMatriz con la fila ordenada:")
    imprimir_matriz(matriz_ejemplo)

if __name__ == "__main__":
    main()
