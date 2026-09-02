import time
class cronometro:
    def __init__(self):
        self.__inicial= time.time()
        self.__finaliza= None
    def getinicial(self):
        return self.__inicial
    def getfinaliza(self):
        return self.__finaliza
    def iniciar(self):
        self.__inicial=time.time()
    def denetener(self):
        self.__finaliza=time.time()
    def lapsotiempo(self):
        return (self.__finaliza-self.__inicial)*1000 
c=cronometro()
print("inicio: ",c.getinicial())
time.sleep(8)
c.denetener()
print("fin: ",c.getfinaliza())
print("timepo ocurrido: ",c.lapsotiempo())