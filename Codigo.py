import random
#definicion de listas 
preguntas_cultura = ["¿Cual es el oceano mas grande del mundo?", 
                     "¿Quien escribio 'Cien anos de soledad'?", 
                     "¿Que metal es mas abundante en la Tierra?", 
                     "¿Quien pinto la Mona Lisa?", 
                     "¿Cual planeta es conocido como el planeta rojo?",
                     "¿Cual es el animal terrestre mas rapido?",
                     "¿En que pais se encuentra la torre Eiffel?",
                     "¿Cual es el idioma nativo mas hablado en el mundo?",
                     "¿En que año llego el hombre a la luna?",
                     "¿Que vitamina se obtiene principalmente del sol?" ]


opciones_cultura = [
    ["a) Atlantico", "b) Indico", "c) Pacifico", "d) Artico"],
    ["a) Gabriel Garcia Marquez", "b) Mario Vargas Llosa", "c) Isabel Allende", "d) Pablo Neruda"],
    ["a) Aluminio", "b) Hierro", "c) Oro", "d) Cobre"],
    ["a) Miguel Angel", "b) Vincent van Gogh", "c) Leonardo da Vinci", "d) Rafael"],
    ["a) Marte", "b) Venus", "c) Saturno", "d) Mercurio"],
    ["a) Guepardo", "b) Leon", "c) Caballo", "d) Leopardo"],
    ["a) Italia", "b) Alemania", "c) Francia", "d) España"],
    ["a) Ingles", "b) Mandarin", "c) Español", "d) Hindi"],
    ["a) 1959", "b) 1965", "c) 1969", "d) 1971"],
    ["a) Vitamina A", "b) Vitamina C", "c) Vitamina D", "d) Vitamina E"]
]

respuestas_cultura = ["c", "a", "a", "c", "a", "a", "c", "b", "c", "c"]

preguntas_capitales = [
    "¿Cual es la capital de Italia?",
    "¿Cual es la capital de Japon?",
    "¿Cual es la capital de Brasil?",
    "¿Cual es la capital de Australia?",
    "¿Cual es la capital de Canada?",
    "¿Cual es la capital de Alemania?",
    "¿Cual es la capital de Egipto?",
    "¿Cual es la capital de Rusia?",
    "¿Cual es la capital de Sudafrica?",
    "¿Cual es la capital de India?"
]

opciones_capitales = [
    ["a) Roma", "b) Milan", "c) Florencia", "d) Venecia"],
    ["a) Kioto", "b) Osaka", "c) Tokio", "d) Nagoya"],
    ["a) Rio de Janeiro", "b) Sao Paulo", "c) Brasilia", "d) Salvador"],
    ["a) Sidney", "b) Melbourne", "c) Canberra", "d) Adelaida"],
    ["a) Toronto", "b) Ottawa", "c) Vancouver", "d) Montreal"],
    ["a) Hamburgo", "b) Munich", "c) Berlin", "d) Frankfurt"],
    ["a) El Cairo", "b) Alejandria", "c) Luxor", "d) Giza"],
    ["a) Moscu", "b) San Petersburgo", "c) Vladivostok", "d) Sochi"],
    ["a) Ciudad del Cabo", "b) Pretoria", "c) Durban", "d) Johannesburgo"],
    ["a) Bombay", "b) Delhi", "c) Calcuta", "d) Nueva Delhi"]
]

respuestas_capitales = ["a", "c", "c", "c", "b", "c", "a", "a", "b", "d"]



def seleccionar_pregunta(categoria_seleccionada, respondidas, categoria):

    # Si es la categoría 2, sumamos 10 a los índices
    if(categoria == 1):
        posicion  = 0
    else:
        posicion  = 10
    
    #  índices de las preguntas no respondidas en la categoría actual
    preguntas_restantes = []
    for i in range(len(categoria_seleccionada)): 
        if (i + posicion ) not in respondidas:
            preguntas_restantes.append(i)


                        
    
    if len(preguntas_restantes) > 0:
        # Selecciona un índice de las preguntas 
        indice_pregunta = random.choice(preguntas_restantes)
        
        # Marca el índice (sumando el posicion  si es necesario) como respondido
        respondidas.append(indice_pregunta + posicion )
        
        # Devuelve la pregunta correspondiente al índice
        return indice_pregunta
    
    # Si ya se han respondido todas las preguntas, devuelve None
    return None



def jugar():
    nombre = input("Ingresa tu nombre: ")
    respondidas = []
    puntaje = 0
    posicion=10 
    while len(respondidas) < 20:

        #Me genera un numero aleatorio entre 1 y 2 para seleccionar la categoria
        numero_categoria = random.randint(1, 2)

        if numero_categoria == 1:
            print("\nCategoria: Cultura General")
            categoria_seleccionada = preguntas_cultura
            opciones_selecionada = opciones_cultura
            respuestas_seleccionada = respuestas_cultura

        else:
            print("\nCategoria: Capitales")
            categoria_seleccionada = preguntas_capitales
            opciones_selecionada = opciones_capitales
            respuestas_seleccionada = respuestas_capitales

        

        indice_pregunta = seleccionar_pregunta(categoria_seleccionada, respondidas, numero_categoria )
        if indice_pregunta is None:
            print("No quedan preguntas en esta categoria.")
            continue


        print(f"{nombre}: {categoria_seleccionada[indice_pregunta]}")

        for opcion in opciones_selecionada[indice_pregunta]:
            print(opcion)

        respuesta = input("Escribe tu respuesta (o 'salir' para terminar el juego): ").lower()

        if respuesta == "salir":
            print(f"\nHas decidido salir del juego, {nombre}.")
            break

        if respuesta == respuestas_seleccionada[indice_pregunta]:
            print("Correcto!")
            puntaje += 2
        else:
            print("Incorrecto.")
            if numero_categoria== 1:
                respondidas.remove (indice_pregunta)
                puntaje -=1
            else :
                  respondidas.remove (indice_pregunta +posicion)
                  puntaje -=1


    print(f"\nJuego terminado, {nombre}. Tu puntaje final es: {puntaje}.")

jugar()
