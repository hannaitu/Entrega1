import random

categorias = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "tipos de datos": ["entero", "float", "bool", "complex"],
    "paises": ["argentina", "francia", "brasil", "canada"]
}

seguir = "si"
#Permite al jugador decidir si quiere seguir jugando o no
while seguir == "si":

    #Mostrar categorias
    print("Categorías disponibles: ")
    for categoria in categorias:
        print("-", categoria)

    #Elige y valida categoria
    eleccion = input("Elegí una categoria: ").strip()
    while eleccion not in categorias:
        eleccion = input("Categoría inválida, elige otra: ")

    print("¡Bienvenido al Ahorcado!")
    print(f"Categoría elegida: {eleccion}")
    print()

    puntaje = 0

    palabras = random.sample(categorias[eleccion], len(categorias[eleccion]))

    #Recorremos cada palabra sin repetirlas
    #Solo se juegan 3 rondas por partida
    for word in palabras[:3]:
        guessed = []
        attempts = 6

        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
                puntaje += 6
                break
            
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            
            letter = input("Ingresá una letra: ").strip().lower()

            #Verifica que el usario no ingrese más de una letra, un número o carárcter inválido
            if len(letter) != 1 or not letter.isalpha():
                print("Entrada no válida.")
                continue
            
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                puntaje -= 1
                print("Esa letra no está en la palabra.")
            
            print()

        #Si el usuario pierde, se termina todo el juego
        else:
            print(f"¡Perdiste! La palabra era: {word}")
            puntaje = 0
            break

    print(f"Tu puntaje fue: {puntaje}")
    seguir = input("¿Querés seguir jugando? (si/no): ").strip().lower()

    #Verifica que el jugador ingrese un dato válido
    while seguir not in ["si", "no"]:
        seguir = input("Ingresá 'si' o 'no': ").strip().lower()
