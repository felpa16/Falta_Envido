print("\nBienvenido al simulador de \033[3mgames de Tenis!")

print("\nPara empezar, defina a sus jugadores.")

jugador1 = input("Jugador 1: ")
jugador2 = input("Jugador 2: ")

puntos_jugador1 = 0
puntos_jugador2 = 0

print("\nAhora elija el modo de simulación.")

modo = input("""
1. Modo Manual
2. Modo Automático

> """)

while (modo != "1" and modo != "2"):
    modo = input("""Error. Por favor elija entre el modo 1 o 2
> """)

def puntaje_manual():
    
    """Imprime a la consola los puntos de cada jugador y le pregunta al usuario quién
    anota el punto siguiente. La respuesta se guarda en la variable 'ganador'.
    """
    print(f"\n{jugador1}: {puntos_jugador1}")
    print(f"{jugador2}: {puntos_jugador2}")
    global ganador
    ganador = input("""¿Quién anota el siguiente punto?
> """)

def puntaje_automatico():
    
    "Imprime los puntos de cada jugador."
    
    print(f"\n{jugador1}: {puntos_jugador1}")
    print(f"{jugador2}: {puntos_jugador2}")

def score(x):
    
    """Crea una tupla con los posibles puntajes que puede tener cada jugador
    y devuelve el valor que contiene una cierta posición ´x´ de la tupla.
    """
    tuple_score = (15, 30, 40, "Ad", "ha ganado el \033[3mgame!")
    return tuple_score[x]

def random_winner():
    
    """Crea una variable 'ganador' a la cual se le 
    asigna un numero aleatorio entre 1 o 2.
    """
    global winner
    winner = random.randint(1,2)


if modo == "1":
    ganador = input("""\n¿Quién anota el punto?
> """)
        
    seguir_jugando = True
    
    while seguir_jugando:
        
        if ganador != jugador1 and ganador != jugador2:
            ganador = input("""\nError. Por favor, ingrese uno de los jugadores
que definió anteriormente 
                           
> """)
                
        if ganador == jugador1:
            
            
            if ganador != jugador1:
               seguir_jugando = False
           
            if puntos_jugador1 == score(4) or puntos_jugador2 == score(4):
                seguir_jugando = False
            
            if puntos_jugador1 == 0:
                puntos_jugador1 = score(0)
                puntaje_manual()
                
    
            elif puntos_jugador1 == 15:
                puntos_jugador1 = score(1)
                puntaje_manual()
                
    
            elif puntos_jugador1 == 30:    
                puntos_jugador1 = score(2)
                puntaje_manual()
                
    
            elif puntos_jugador1 == 40 and puntos_jugador2 != 40 and puntos_jugador2 != "Ad":
                puntos_jugador1 = score(4)
                print("\n" + jugador1, puntos_jugador1)
                seguir_jugando = False
                
                
            elif puntos_jugador1 == 40 and puntos_jugador2 == 40:    
                puntos_jugador1 = score(3)
                puntaje_manual()
                
                              
            elif puntos_jugador1 == "Ad" and puntos_jugador2 == 40:
                puntos_jugador1 = score(4)
                print("\n" + jugador1, puntos_jugador1)
                seguir_jugando = False
                
            elif puntos_jugador1 == 40 and puntos_jugador2 == "Ad":
                puntos_jugador2 = score(2)
                puntaje_manual()
                
                    
        elif ganador == jugador2:
            
            if ganador != jugador2:
               seguir_jugando = False 
           
            if puntos_jugador1 == score(4) or puntos_jugador2 == score(4):
                seguir_jugando = False
            
            if puntos_jugador2 == 0:
                puntos_jugador2 = score(0)
                puntaje_manual()
            
    
            elif puntos_jugador2 == 15:
                puntos_jugador2 = score(1)
                puntaje_manual()
            
    
            elif puntos_jugador2 == 30:    
                puntos_jugador2 = score(2)
                puntaje_manual()
            
    
            elif puntos_jugador2 == 40 and puntos_jugador1 != 40 and puntos_jugador1 != "Ad":
                puntos_jugador2 = score(4)
                print("\n" + jugador2, puntos_jugador2)
                seguir_jugando = False
                
                
            elif puntos_jugador2 == 40 and puntos_jugador1 == 40:    
                puntos_jugador2 = score(3)
                puntaje_manual()
            
                    
            elif puntos_jugador2 == "Ad" and puntos_jugador1 == 40:
                puntos_jugador2 = score(4)
                print("\n" + jugador2, puntos_jugador2)
                seguir_jugando = False
            
            elif puntos_jugador1 == "Ad" and puntos_jugador2 == 40:
                puntos_jugador1 = score(2)
                puntaje_manual()
                

if modo == "2":
    
    length = input("""\n¿Cómo quiere ver el resultado del \033[3mgame? 

1. En Detalle
2. Solo el ganador

> """)
    
    import random
        
    random_winner()
    
    seguir_jugando = True
    
    while length != "1" and length != "2":
        length = input("""\nError. Por favor, elija entre la opción 1 o 2 
                       
> """)
    while seguir_jugando == True:
        
        if length == "1":
        
            if winner == 1:
            
                if winner != 1:
                    seguir_jugando = False
                
                if puntos_jugador1 == score(4) or puntos_jugador2 == score(4):
                    seguir_jugando = False
            
                if puntos_jugador1 == 0:
                    puntos_jugador1 = score(0)
                    puntaje_automatico()
                    random_winner()
                
                elif puntos_jugador1 == 15:
                    puntos_jugador1 = score(1)
                    puntaje_automatico()
                    random_winner()
            
                elif puntos_jugador1 == 30:
                    puntos_jugador1 = score(2)
                    puntaje_automatico()
                    random_winner()
                
                elif puntos_jugador1 == 40 and puntos_jugador2 != 40 and puntos_jugador2 != "Ad":
                    puntos_jugador1 = score(4)
                    print("\n" + jugador1, puntos_jugador1)
                    seguir_jugando = False
                
                elif puntos_jugador1 == 40 and puntos_jugador2 == 40:
                    puntos_jugador1 = score(3)
                    puntaje_automatico()
                    random_winner()
                    
                elif puntos_jugador1 == 40 and puntos_jugador2 == "Ad":
                    puntos_jugador2 = score(2)
                    puntaje_automatico()
                    random_winner()
                    
                elif puntos_jugador1 == "Ad" and puntos_jugador2 == 40:
                    puntos_jugador1 = score(4)
                    print("\n" + jugador1, puntos_jugador1)
                    seguir_jugando = False
                    
                
        
            if winner == 2:
                
                if winner != 2:
                    seguir_jugando = False
                
                if puntos_jugador1 == score(4) or puntos_jugador2 == score(4):
                    seguir_jugando = False
            
                if puntos_jugador2 == 0:
                    puntos_jugador2 = score(0)
                    puntaje_automatico()
                    random_winner()
                
                elif puntos_jugador2 == 15:
                    puntos_jugador2 = score(1)
                    puntaje_automatico()
                    random_winner()
            
                elif puntos_jugador2 == 30:
                    puntos_jugador2 = score(2)
                    puntaje_automatico()
                    random_winner()
                
                elif puntos_jugador2 == 40 and puntos_jugador1 != 40 and puntos_jugador1 != "Ad":
                    puntos_jugador2 = score(4)
                    print("\n" + jugador2, puntos_jugador2)
                    seguir_jugando = False
                
                elif puntos_jugador2 == 40 and puntos_jugador1 == 40:
                    puntos_jugador2 = score(3)
                    puntaje_automatico()
                    random_winner()
                    
                elif puntos_jugador2 == 40 and puntos_jugador1 == "Ad":
                    puntos_jugador1 = score(2)
                    puntaje_automatico()
                    random_winner()
                    
                elif puntos_jugador2 == "Ad" and puntos_jugador1 == 40:
                    puntos_jugador2 = score(4)
                    print("\n" + jugador2, puntos_jugador2)
                    seguir_jugando = False
                    
        if length == "2":
            
            if winner == 1:
            
                if winner != 1:
                    seguir_jugando = False
            
                if puntos_jugador1 == score(4) or puntos_jugador2 == score(4):
                    seguir_jugando = False
            
                if puntos_jugador1 == 0:
                    puntos_jugador1 = score(0)
                    random_winner()
                
                elif puntos_jugador1 == 15:
                    puntos_jugador1 = score(1)
                    random_winner()
            
                elif puntos_jugador1 == 30:
                    puntos_jugador1 = score(2)
                    random_winner()
                
                elif puntos_jugador1 == 40 and puntos_jugador2 != 40:
                    puntos_jugador1 = score(4)
                    print("\n" + jugador1, puntos_jugador1)
                    seguir_jugando = False
                
                elif puntos_jugador1 == 40 and puntos_jugador2 == 40:
                    puntos_jugador1 = score(3)
                    random_winner()
                    
                elif puntos_jugador1 == 40 and puntos_jugador2 == "Ad":
                    puntos_jugador2 = score(2)
                    random_winner()
                    
                elif puntos_jugador1 == "Ad" and puntos_jugador2 == 40:
                    puntos_jugador1 = score(4)
                    print("\n" + jugador1, puntos_jugador1)
                    seguir_jugando = False
                    
        
            if winner == 2:
                
                if winner != 2:
                    seguir_jugando = False
                
                if puntos_jugador1 == score(4) or puntos_jugador2 == score(4):
                    seguir_jugando = False
            
                if puntos_jugador2 == 0:
                    puntos_jugador2 = score(0)
                    random_winner()
                
                elif puntos_jugador2 == 15:
                    puntos_jugador2 = score(1)
                    random_winner()
            
                elif puntos_jugador2 == 30:
                    puntos_jugador2 = score(2)
                    random_winner()
                
                elif puntos_jugador2 == 40 and puntos_jugador1 != 40:
                    puntos_jugador2 = score(4)
                    print("\n" + jugador2, puntos_jugador2)
                    seguir_jugando = False
                
                elif puntos_jugador2 == 40 and puntos_jugador1 == 40:
                    puntos_jugador2 = score(3)
                    random_winner()
                    
                elif puntos_jugador2 == 40 and puntos_jugador1 == "Ad":
                    puntos_jugador1 = score(2)
                    random_winner()
                    
                elif puntos_jugador2 == "Ad" and puntos_jugador1 == 40:
                    puntos_jugador2 = score(4)
                    print("\n" + jugador2, puntos_jugador2)
                    seguir_jugando = False

