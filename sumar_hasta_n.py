#ALGORITMO: sumar_hasta_n
#ENTRADA: n
#SUMA: suma

# suma = 0
# contador = 1
# MIENTRAS contador <= n:
#     suma = suma + contador
#     contador = contador + 1
# DEVOLVER suma
def suma_hasta_n(n):
    suma = 0
    contador = 1

    while contador <= n:
        suma = suma + contador
        contador = contador + 1

    return suma
#EJECUCIÓN
print(suma_hasta_n(5))
print(suma_hasta_n(3))