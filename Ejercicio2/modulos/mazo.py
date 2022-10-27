# Importo Cola Doble para la implementaciÃ³n del Mazo
from cola_doble import ColaDoble

# Importaciones para pruebas locales
from carta import Carta
import random as rd


class Mazo:
    
    def __init__(self):
        self.mazo = ColaDoble()
    
    # MÃ©todos MÃ¡gicos
    
    def __str__(self):
        return str(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)
    
    
    # MÃ©todos
    
    def tamanio(self):
        return self.mazo.tamanio
    
    def agregar_carta(self, cartaNueva):
        '''
        Recibe una carta, y la agrega al mazo.

        Parameters
        ----------
        cartaNueva : class
            Recibe una carta.

        Returns
        -------
        None.

        '''
        self.mazo.agregarFrente(cartaNueva)
        
    def jugar_carta(self, estadoCara="Boca abajo"):
        '''
        Remueve la carta que se encuentra en el frente del mazo,
        y la devuelve. Dependiendo del estado, estarÃ¡ Boca arriba,
        o Boca abajo.

        Parameters
        ----------
        estadoCara : class, opcional
            Si los jugadores estÃ¡n en guerra, se deja la carta
            boca abajo, sino se recibe como parámetro "Boca arriba".
            Por defecto la cara de la carta es "Boca abajo".

        Returns
        -------
        cartaJugada : class
            Retorna la carta que se jugó.

        '''
        cartaJugada = self.mazo.removerFrente()
        cartaJugada.estadoCara = estadoCara
        
        return cartaJugada
    
    def ganar_carta(self, cartasGanadas):
        self.mazo.agregarFinal(cartasGanadas)

    def sacar_carta(self):
        return self.mazo.removerFrente()



# Pruebas locales

if __name__ == "__main__":
    
    mazo = Mazo()
    mazoJ1 = Mazo()
    mazoJ2 = Mazo()
    
    '''Crear Mazo'''
    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
    cartas = []     # Lista para guardar las cartas, mezclarlas y luego crear un mazo
    jerarquia = 0   # Utilizo una jerarquÃ­a para comparar luego las cartas
        
    # Asigno cada nÃºmero a los 4 palos
    for numero in valores:
        jerarquia+=1    # Aumento la jerarquÃ­a por cada iteraciÃ³n
        
        for palo in palos:
            carta = Carta(palo, numero, jerarquia, "Boca arriba")  # Creo una carta y le paso los parÃ¡metros correspondientes
            cartas.append(carta)    # Agrego la carta a la lista de cartas para crear luego el mazo
        
    rd.shuffle(cartas)      # Mezclo las cartas
        
    # Una vez mezcladas las cartas, las agrego al mazo
    for carta in cartas:
        mazo.agregar_carta(carta)
        
    print("\nMazo:\n", mazo)
    
    
    
    '''Repartir cartas'''
    
    for i, carta in enumerate(mazo):
        '''
        Si "i" es par, la carta va al mazo del Jugador 1,
        si es impar, la carta va al mazo del Jugador 2.
        '''
        if i%2 == 0:
            mazoJ1.agregar_carta(carta)
                
        if i%2 != 0:
            mazoJ2.agregar_carta(carta)
                
    
    print("\nMazo Jugador 1:\n", mazoJ1)
    print("\nMazo Jugador 2:\n", mazoJ2)
