from jugador import Jugador


def test_constructor_sin_fichas():
    j = Jugador("tomas")
    assert(j.nombre == "tomas")
    assert(j.fichas == 5)

def test_dar_ficha():
    j = Jugador("tomas", 10)
    j.darFicha(5)
    assert(j.fichas == 15)

jugador1 = Jugador("tomas", 10)
print(jugador1)

try:
    jugador1.sacarFicha(5)
    print(jugador1)
    jugador1.sacarFicha(6)
except ValueError as e:
    print(e)


def test_tiene_ficha():
    j = Jugador("Tomas", 10)
    assert(j.tieneFicha())  #True

    assert(j.tieneFicha(5))  #True

    assert(j.tieneFicha(11))  #False


#tomas = Jugador("tomas", 15)
#print(tomas) 






