class Sensor:
    tipo = "Genérico"
    def __init__(self, id_sensor):
        self.id = id_sensor
        self.encendido = False
    def activar(self):
        self.encendido = True
    def desactivar(self):
        self.encendido = False
class Camara(Sensor):
    tipo = "Cámara"
    def __init__(self, id_sensor, resolucion):
        super().__init__(id_sensor)
        self.resolucion = resolucion
class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"
    def __init__(self, id_sensor, alcance):
        super().__init__(id_sensor)
        self.alcance = alcance
class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"
    def __init__(self, id_sensor, resolucion, alcance):
        Camara.__init__(self, id_sensor, resolucion)
        SensorLuzLaser.__init__(self, id_sensor, alcance)
if __name__ == "__main__":
    print("--- Sistema de Vehículo Autónomo ---")
    auto = VehiculoAutonomo("S-01", "1080p", 50)
    print(f"ID: {auto.id}")
    print(f"Tipo: {auto.tipo}")
    print(f"Resolución: {auto.resolucion}")
    print(f"Alcance: {auto.alcance}m")
    auto.activar()
    print(f"¿Está encendido?: {auto.encendido}")