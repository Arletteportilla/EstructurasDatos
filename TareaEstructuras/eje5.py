def esta_ordenado_ascendente(arreglo):
    # Iteramos sobre cada elemento del arreglo
    for i in range(1, len(arreglo)):
        # Verificamos si el elemento actual es menor o igual al anterior
        if arreglo[i] < arreglo[i-1]:
            return False
            
    # Si no se encontró ningún par de elementos desordenados, el arreglo está ordenado
    return True