class Jugador:
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre 
        self.fichas = fichas 

    def __repr__(self):
        return f"{self.nombre}, {self.fichas} fichas"

    def darFicha(self, cantidad=1):
        self.fichas += cantidad

    def sacarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError("No puedes sacar más fichas de las que tienes.")
        self.fichas -= cuantas

    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas
    


