def calcular_decuento(monto_total, porcentaje_decuento=15):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Args:
        monto_total (float): Monto total de la compra
        porcentaje_decuento (float, optional): Porcentaje de descuento. Por defecto

    Returns:
        float: Monto del decuento calculado.
    """
    descuento = monto_total * (porcentaje_decuento / 100)
    return descuento

#Llamadas a la función calcular_descuento desde el programa principal
monto_compra1 = 1500
descuento1 = calcular_decuento(monto_compra1)
print(f"Descuento aplicado en la compra de ${monto_compra1}: ${descuento1}")

monto_compra2 = 3500
porcentaje_decuento2 = 20
descuento2 = calcular_decuento(monto_compra2, porcentaje_decuento2)
print(f"Descuento aplicado en la compra de ${monto_compra2} con {porcentaje_decuento2}% de descuento: ${descuento2}")