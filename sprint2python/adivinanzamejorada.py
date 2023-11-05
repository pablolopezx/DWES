import random

comprespuesta = ""  
def adivinanza_aleatoria():
    adivinanzas = [
        """Quien lo fabrica, no lo necesita. Quien lo compra, no lo necesita. Quien lo usa, no lo ve ni lo siente. ¿Qué es?
    
    a)Un bolígrafo
    b)Un ataúd
    c)Un pollo""",
        """Si me dejas caer, seguro que me parto. Dame una sonrisa, y siempre te devolveré otra. ¿Qué soy?

    a)Un espejo
    b)Un diamante
    c)Un lapiz""",
         """¿Cuántos meses tienen 28 días?

    a)Todos
    b)Diciembre
    c)Febrero"""
    ]
    respuestas = [
        "b",
        "a",
        "a"
    ]
    #Definidas adivinanzas y respuestas
    # Elige dos adivinanzas al azar sin repetición
    adivinanzas_elegidas = random.sample(adivinanzas, 2)
    puntos =0 #Definir puntos
    for i, adivinanza in enumerate(adivinanzas_elegidas):
        print(adivinanza)
        respuesta = input("¿Cuál es tu respuesta? ")

        # Compara la respuesta del usuario con la respuesta esperada
        if respuesta.lower() == respuestas[adivinanzas.index(adivinanza)].lower():
            print("¡Respuesta correcta!")
            puntos = puntos +10
        else: #Mostrar al usuario la respuesta correcta si no acierta
            print("Respuesta incorrecta. La respuesta correcta es:", respuestas[adivinanzas.index(adivinanza)])
            puntos = puntos -5
        
    print("Juego terminado! Puntos:"+str(puntos))
if __name__ == "__main__":
    adivinanza_aleatoria()




