# Exercici 25: crear un fitxer vehicle.py 
# definir la classe vehicle amb: constructor, 6 atributs,
# Getters i Setters, mètode per mostrar totes les dades
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
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca
    
    