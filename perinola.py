from random import choice,randint

class Perinola:

    def __init__(self):
        self.cara_visible= 'Pon 1'
    
    def __repr__(self):
        return f"salio : {self.cara_visible}"
    
    def tirar(self):
       msj = ('Pon 1','Pon 2','Toma 1','Toma 2','Todos Toman','Ponen Todos')
       self.cara_visible = choice(msj)
       return self.cara_visible
    
    def tirar(self):
       resulObtenido = randint (self.cara_visible)
       return resulObtenido