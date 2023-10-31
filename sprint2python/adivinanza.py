puntos= 0
print (
    """Quien lo fabrica, no lo necesita. Quien lo compra, no lo necesita. Quien lo usa, no lo ve ni lo siente. ¿Qué es?
    
    a)Un bolígrafo
    b)Un ataúd
    c)Un pollo"""
)
respuesta = input( "tu respuesta? (a,b,c)")
if respuesta == "b":
    print("Respuesta Correcta")
    puntos = puntos+10
else: 
    print("Respuesta Incorrecta") 
    puntos = puntos -5

print (
    """Si me dejas caer, seguro que me parto. Dame una sonrisa, y siempre te devolveré otra. ¿Qué soy?

    a)Un espejo
    b)Un diamante
    c)Un lapiz"""
)
respuesta = input( "tu respuesta? (a,b,c)")
if respuesta == "a":
    print("Respuesta Correcta")
    puntos = puntos+10
else: 
    print("Respuesta Incorrecta") 
    puntos = puntos -5

print (
    """¿Cuántos meses tienen 28 días?

    a)Todos
    b)Diciembre
    c)Febrero"""
)
respuesta = input( "tu respuesta? (a,b,c)")
if respuesta == "a":
    print("Respuesta Correcta")
    puntos = puntos+10
else: 
    print("Respuesta Incorrecta") 
    puntos = puntos -5
texto = "Juego finalizado!" + "\n" + "Puntos conseguidos:" + str(puntos)
print(texto)