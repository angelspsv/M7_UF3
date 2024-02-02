# Exercici 26: crear un fitxer user.py 
# definir la classe user amb: constructor, 6 atributs,
# Getters i Setters, mètode Salutacio per mostrar 
# totes les dades/atributs del objecte user,
# afegir el mètode to_dict(self) per retornar l'objecte
# en format json
import json
class user:
    def __init__(self, nom, cognom, sexe, edat, mail, telf):
        self.nom = nom
        self.cognom = cognom
        self.sexe = sexe
        self.edat = edat
        self.mail = mail
        self.telf = telf

    #mètodes getters i setters
    def getNom(self):
        return self.nom
    
    def setNom(self, nom):
        self.nom = nom
    
    def getCognom(self):
        return self.cognom
    
    def setCognom(self, cognom):
        self.cognom = cognom

    def getSexe(self):
        return self.sexe
    
    def setSexe(self, sexe):
        self.sexe = sexe
    
    def getEdat(self):
        return self.edat
    
    def setEdat(self, edat):
        self.edat = edat

    def getMail(self):
        return self.mail
    
    def setMail(self, mail):
        self.mail = mail

    def getTelf(self):
        return self.telf
    
    def setTelf(self, telf):
        self.telf = telf

    #mètode Salutacio que mostra totes les dades del objecte
    def Salutacio(self):
        return {
            'nom': self.nom,
            'cognom': self.cognom,
            'sexe': self.sexe,
            'edat': self.edat,
            'mail': self.mail,
            'telf': self.telf
        }

    # aquest mètode retorna l'objecte en format json
    def to_dict(self):
        atributs = {
            "nom": self.nom,
            "cognom": self.cognom,
            "sexe": self.sexe,
            "edat": self.edat,
            "mail": self.mail,
            "telf": self.telf
        }
        return json.dumps(atributs, indent=2)



#persona1 = user("David", "Lopez", "home", 22, "david@mail.com", "612345678")
#dades_persona = persona1.Salutacio()
#print(dades_persona)
#dades_persona_json = persona1.to_dict()
#print(dades_persona_json)