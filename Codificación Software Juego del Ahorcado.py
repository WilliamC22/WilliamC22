





import random


palabras = ['python', 'programacion', 'computadora', 'desarrollo', 'tecnologia', 'inteligencia']
def obtener_palabra():
    #Toma una palabra aleatoria de la lista anterior
    return random.choice(palabras)
def mostrar_tablero(palabra, letras_adivinadas):
    tablero = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + ' '
        else:
            tablero += '_ '
    return tablero 

def jugar_ahorcado():
    palabra = obtener_palabra()
    letras_adivinadas = []
    intentos = 7 

    print("¡Bienvenido al Juego del Ahorcado!")
    print("Tienes que adivinar una palabra aleatoria.")
    print(mostrar_tablero(palabra, letras_adivinadas))

    while intentos > 0:
        letra = input("Ingresa una letra: ").lower()
        if letra in letras_adivinadas:
            print("Ya has ingresado esa letra. ¡Intenta con otra!")  
            continue  
        if letra not in palabra:
             intentos -= 1
             print("Letra incorrecta. Te quedan {} intentos.".format(intentos))

        print(mostrar_tablero(palabra, letras_adivinadas))

        if all(letra in letras_adivinadas for letra in palabra):
            print("¡Muy bien! Has adivinado la palabra: '{}'".format(palabra))
jugar_ahorcado()