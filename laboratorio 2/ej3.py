import math
class Vector3D:
    def __init__(self,a1=0.0,a2=0.0,a3=0.0):
        self.a1=float(a1)
        self.a2=float(a2)
        self.a3=float(a3)
    def __add__(self, b):
        return Vector3D(self.a1+b.a1,self.a2+b.a2,self.a3+b.a3)
    def __mul__(self, other):
        if isinstance(other,(int,float)):
            return Vector3D(self.a1*other,self.a2*other,self.a3*other)
        elif isinstance(other,Vector3D):
            return self.a1*other.a1+self.a2*other.a2+self.a3*other.a3
        return NotImplemented
    def __rmul__(self, r):
        return self.__mul__(r)
    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)
    def __abs__(self):
        return self.magnitud()
    def normal(self):
        mag = self.magnitud()
        if mag==0:
            raise ValueError("No se puede normalizar el vector nulo.")
        return Vector3D(self.a1/mag,self.a2/mag,self.a3/mag)
    def __xor__(self, b):
        return Vector3D(
            self.a2*b.a3-self.a3*b.a2,
            self.a3*b.a1-self.a1*b.a3,
            self.a1*b.a2-self.a2*b.a1
        )
    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"
if __name__ == "__main__":
    a = Vector3D(1,2,3)
    b = Vector3D(4,5,6)
    print("Vector a=",a)
    print("Vector b=",b)
    print("a+b=",a+b)
    print("3*a=",3*a)
    print("Longitud de a (|a|):",abs(a))
    print("Normal de a:",a.normal())
    print("Producto escalar (a·b):", a*b)
    print("Producto vectorial (a^b):",a**b)