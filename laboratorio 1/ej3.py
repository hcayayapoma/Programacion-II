class cuadrantricas:
    def calcular(self):
        pass
class variables(cuadrantricas):
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def conseguirdet(self):
        determinante=self.__b**2-4*self.__a*self.__c
        return determinante
    def conseguirraiz1(self):
        raiz1=(-self.__b+(self.__b**2-4*self.__a*self.__c)**(1/2))/(self.__a*2)
        return raiz1
    def conseguirraiz2(self):
            raiz2=(-self.__b-(self.__b**2-4*self.__a*self.__c)**(1/2))/(self.__a*2)
            return raiz2
listas=["a","b","c"]
l={}
for i in listas:
    l[i]=float(input("ingrese los valores para la ecuacion cuadrantica: "))
sistema=variables(*l.values())
discrinar= sistema.conseguirdet()
if discrinar>0:
     print("la ecuacion tiene dos raices: ",sistema.conseguirraiz1()," y ",sistema.conseguirraiz2())
elif discrinar==0:
     print("la ecuacion solo tiene 1 raiz: ",sistema.conseguirraiz1())
else:
     print("la ecuacion no tiene reales")