class varibales:
    def calcular(self):
        pass
class numeros(varibales):
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.f=f
    def tienesolucion(self):
        return (self.a*self.d)-(self.b*self.c)
        ##return true
    def conseguirx(self):
        determinar=self.tienesolucion()
        if determinar==0:
            return None
        return (self.e*self.d-self.b*self.f)/determinar
    def conseguiry(self):
        determinar=self.tienesolucion()
        if determinar==0:
            return None
        return (self.a*self.f-self.e*self.c)/determinar
        
valores=['a', 'b', 'c', 'd', 'e', 'f']
lista={}
for i in valores:
    lista[i]=float(input("ingrese los numeros de las variables:"))
sistema=numeros(*lista.values())
comprobar=sistema.tienesolucion()
if comprobar==True:
    print("la ecuacion no tiene solucion")
else:
    print(f"la respuesta de x es: {sistema.conseguirx()}")
    print(f"la respuesta de y es: {sistema.conseguiry()}")






































class varibales:
    def calcular(self):
        pass

class numeros(varibales):
    def __init__(self, a, b, c, d, e, f):
        # 1. Atributos privados (Punto A y B)
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # 2. Devuelve un Booleano True/False (Punto C)
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0

    # 3. Métodos renombrados a getX() y getY() (Punto D)
    def getX(self):
        det = (self.__a * self.__d - self.__b * self.__c)
        if det == 0:
            return None
        return (self.__e * self.__d - self.__b * self.__f) / det

    def getY(self):
        det = (self.__a * self.__d - self.__b * self.__c)
        if det == 0:
            return None
        return (self.__a * self.__f - self.__e * self.__c) / det

# --- Tu captura de datos con el bucle for ---
valores = ['a', 'b', 'c', 'd', 'e', 'f']
lista = {}

for i in valores:
    lista[i] = float(input(f"ingrese el numero para {i}: "))

sistema = numeros(*lista.values())

# 4. Evaluación corregida
if sistema.tieneSolucion():
    print(f"la respuesta de x es: {sistema.getX()}")
    print(f"la respuesta de y es: {sistema.getY()}")
else:
    print("la ecuacion no tiene solucion")