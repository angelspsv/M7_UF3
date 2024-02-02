# Exercici 25: crear un fitxer vehicle.py 
# definir la classe vehicle amb: constructor, 6 atributs,
# Getters i Setters, mètode per mostrar totes les dades,
# afegir el mètode to_dict(self) per retornar l'objecte
# en format json
class vehicle:
    def __init__(self, marca, modelo, any, color, vel_max, combustible):
        self.marca = marca
        self.model = modelo
        self.any = any
        self.color = color
        self.vel_max = vel_max
        self.combustible = combustible
    
    # mètodes get i set per accedir als atributs
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getAny(self):
        return self.any
    
    def setAny(self, any):
        self.any = any
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
    
    def getVel(self):
        return self.vel_max
    
    def setVel(self, vel_max):
        self.vel_max = vel_max
    
    def getCombustible(self):
        return self.combustible
    
    def setCombustible(self, combustible):
        self.combustible = combustible
    
    # mètode que retorna un diccionari amb els valors de l'objecte
    def parts(self):
        return {
            'marca': self.marca,
            'modelo': self.modelo,
            'any': self.any,
            'color': self.color,
            'vel_max': self.vel_max,
            'combustible': self.combustible
        }

