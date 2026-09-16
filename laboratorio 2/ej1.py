import math
class mipunto:
    def __init__(self, x=0.0, y=0.0):
        self._x=float(x)
        self._y=float(y)
    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def distancia(self,*args):
        if len(args)==1 and isinstance(args[0],mipunto):
            otro=args[0]
            return math.sqrt((otro.get_x()-self._x)**2 + (otro.get_y()-self._y)**2)
        elif len(args)==2:
            x2,y2=args[0],args[1]
            return math.sqrt((x2-self._x)**2+(y2-self._y)**2)
        else:
            raise ValueError("Parámetros inválidos para calcular la distancia.")
if __name__=="__main__":
    p1=mipunto()           
    p2=mipunto(10, 20.5) 
    print(f"Distancia entre p1 y p2: {p1.distancia(p2):.4f}")
    print(f"Distancia usando coordenadas (10, 20.5): {p1.distancia(10, 20.5):.4f}")