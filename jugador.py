class Jugador:
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre 
        self.fichas = fichas 

    def __repr__(self):
        return f"{self.nombre}, {self.fichas} fichas"

    def darFicha(self, cantidad=1):
        self.fichas += cantidad
