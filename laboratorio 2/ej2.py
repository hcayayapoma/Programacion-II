import math
class AlgebraVectorial:
    def __init__(self,x=0.0,y=0.0):
        self.x=float(x)
        self.y=float(y)
    def magnitud(self):
        return math.sqrt(self.x**2+self.y**2)
    def producto_punto(self,b):
        return self.x*b.x+self.y*b.y
    def es_perpendicular_a(self, b):
        suma=AlgebraVectorial(self.x+b.x,self.y+b.y)
        resta=AlgebraVectorial(self.x-b.x,self.y-b.y)
        return math.isclose(suma.magnitud(),resta.magnitud(),abs_tol=1e-9)
    def es_perpendicular_c(self,b):
        return math.isclose(self.producto_punto(b),0.0,abs_tol=1e-9)
    def es_paralela_e(self,b):
        if b.x!=0 and b.y!= 0:
            return math.isclose(self.x/b.x,self.y/b.y,abs_tol=1e-9)
        return False
    def es_paralela_f(self,b):
        cruz=self.x*b.y-self.y*b.x
        return math.isclose(cruz,0.0,abs_tol=1e-9)
    def proyeccion_sobre(self, b):
        mag_b_cuad=b.magnitud()**2
        if mag_b_cuad==0:
            raise ValueError("No se puede proyectar sobre el vector nulo.")
        escalar=self.producto_punto(b)/mag_b_cuad
        return AlgebraVectorial(escalar*b.x,escalar*b.y)
    def componente_en(self, b):
        mag_b = b.magnitud()
        if mag_b == 0:
            raise ValueError("El vector de referencia no puede ser nulo.")
        return self.producto_punto(b) / mag_b
    def __str__(self):
        return f"({self.x},{self.y})"
if __name__=="__main__":
    a = AlgebraVectorial(3, 4)
    b = AlgebraVectorial(-4, 3)
    print("Vector a:", a)
    print("Vector b:", b)
    print("¿Son perpendiculares (a · b = 0)?:", a.es_perpendicular_c(b))
    print("Proyección de 'a' sobre 'b':", a.proyeccion_sobre(b))
    print("Componente de 'a' en 'b':", a.componente_en(b))