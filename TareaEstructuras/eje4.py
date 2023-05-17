def contar_mayores_que_promedio(arreglo):
    # Calculamos el promedio de los números del arreglo
    promedio = sum(arreglo) / len(arreglo)
    
    # Contamos los números mayores que el promedio
    cantidad = 0
    for numero in arreglo:
        if numero > promedio:
            cantidad += 1
            
    return cantidad