from claseJugador import Jugador

class ManejadorJugadores:
    __jugadores = []

    def __init__(self):
        self.__jugadores = []

    def agregaJugador(self, jugador):
        if isinstance(jugador, Jugador):
            self.__jugadores.append(jugador)

