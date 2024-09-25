class Apuesta:


     def __init__(self):
           self.fichas = 0


     def __repr__(self):
       return f" Apuesta: {self.fichas}"     
 

     def ponerFicha(self, cuantas = 1):
         if cuantas < self.fichas :                                                                            
           raise ValueError("Error")
    
     def tomarFichas(self, cuantas =1):
         if cuantas > self.fichas:
             raise ValueError("Error")
         self.fichas -= cuantas
     def tomarTodas(self):
      cantidad = self.fichas
      self.fichas = 0
      return cantidad
    
     def tieneFicha(self, cuantas =1):
         return self.fichas >= cuantas
     
     def estaVacia(self):
         return self.fichas == 0
