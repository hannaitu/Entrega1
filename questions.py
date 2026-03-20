import random

categorias = {
    "Programación": ["python", "variable", "función", "bucle"],
    "Tipos de Datos": ["entero", "float", "bool", "complex"],
    "Países": ["Argentina", "francia", "brasil", "canada"]
}

#Mostrar categorias
print("Categorías disponibles: ")
for categoría in categorias:
    print("-", categoría)

#Elige y valida categoria
eleccion = input("Elegí una categoria: ")
while eleccion not in categorias:
    eleccion = input("Categoría inválida, elige otra: ")

print("¡Bienvenido al Ahorcado!")
print()

puntaje = 0

palabras = random.sample(categorias[eleccion], len(categorias[eleccion]))

#Recorremos cada palabra sin repetirlas
for word in palabras:
    word = word.lower()
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
        
        letter = input("Ingresá una letra: ").lower()

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

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0

print(f"Tu puntaje fue: {puntaje}")
