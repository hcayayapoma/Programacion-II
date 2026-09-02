import math
class Estadistica:
    def __init__(self, datos):
        self.datos = datos
    def promedio(self):
        return sum(self.datos) / len(self.datos)
    def desviacion(self):
        prom = self.promedio()
        n = len(self.datos)
        suma_diferencias = sum((x - prom) ** 2 for x in self.datos)
        return math.sqrt(suma_diferencias / (n - 1))
entrada = input("Ingrese 10 números separados por espacio: ")
numeros = [float(x) for x in entrada.split()]
est = Estadistica(numeros)
print(f"El promedio es {est.promedio():.2f}")
print(f"La desviacion estandard es {est.desviacion():.5f}")