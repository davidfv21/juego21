import random

def baraja():
    return random.sample([(x,y) for x in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] for y in ["Diamantes","Corazones","Picas","Treboles"]],52)

def valorCarta(carta, acumulado):
    if(carta[0]=="J" or carta[0]=="Q" or carta[0]=="K"):
        return 10
    if carta[0]=="A" and acumulado+11>21:
        return 1
    else:
        return int(carta[0])

def calcularMano(listaDeCartas, acumulado):
            if len(listaDeCartas)==1:
                return valorCarta(listaDeCartas[0], acumulado)
            else:
                return valorCarta(listaDeCartas[0], acumulado)+calcularMano(listaDeCartas[1:],acumulado+valorCarta(listaDeCartas[0],acumulado))


def juego(cartasJugador, cartasRepartidor, contador):
    if(contador==1):
        print "JUGADOR"
        print "\nCartas repartidor : Carta Oculta "+str(cartasRepartidor[1])
        print "\nSus cartas son "+str(cartasJugador)
        print "\nPuntaje: "+str(calcularMano(cartasJugador,0))
        if(calcularMano(cartasJugador,0)<21):
            if(input("otra carta? 1.Tomar 2.Plantar")==1):
                juego(cartasJugador+baraja()[:1],cartasRepartidor,contador)
            else:
                juego(cartasJugador,cartasRepartidor,2)
        elif(calcularMano(cartasJugador,0)==21):
            juego(cartasJugador,cartasRepartidor,2)
        else:
            print "el repartidor gana"
    elif(contador==2):
        print "repartidor"
        print "\nSus cartas son: "+str(cartasJugador)
        print "\nPuntaje: "+str(calcularMano(cartasJugador,0))
        print "\nCartas repartidor: "+str(cartasRepartidor)
        print "\nPuntaje: "+str(calcularMano(cartasRepartidor,0))
        if(calcularMano(cartasRepartidor,0)<21):
            if(calcularMano(cartasRepartidor,0)<calcularMano(cartasJugador,0)):
                juego(cartasJugador,cartasRepartidor+baraja()[:1],contador)
            else:
                juego(cartasJugador,cartasRepartidor,3)
        elif(calcularMano(cartasRepartidor,0)==21):
            print "el repartidor gana"
        else:
            print "El jugador gana"
    else:
        print ""
        if(calcularMano(cartasRepartidor,0)<calcularMano(cartasJugador,0)):
            print "El jugador gana"
        elif(calcularMano(cartasRepartidor,0)>=calcularMano(cartasJugador,0)):
            print "el repartidor gana"

juego(baraja()[:2], baraja()[:2],1)
