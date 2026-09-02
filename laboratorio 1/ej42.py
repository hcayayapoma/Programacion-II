import math
def promedio(valores):
    return sum(valores) / len(valores)
def desviacion(valores):
    prom = promedio(valores)
    n = len(valores)
    suma_diferencias = sum((x - prom) ** 2 for x in valores)
    return math.sqrt(suma_diferencias / (n - 1))
entrada = input("Ingrese 10 números separados por espacio: ")
numeros = [float(x) for x in entrada.split()]
print(f"El promedio es {promedio(numeros):.2f}")
print(f"La desviacion estandard es {desviacion(numeros):.5f}")