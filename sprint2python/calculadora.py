from operaciones import suma, resta, multiplicacion, division
if __name__ == "__main__":
    otra= "s"
    while otra == "s":
        numero1 = input("numero1?")
        numero2 = input("numero2?")
        numero1= int(numero1)    
        numero2= int(numero2)
        operacion = input("""Operacion a realizar?
        1.-Suma
        2.-Resta
        3.-Multiplicacion
        4.-Division
                          """)
        if operacion == "1":
            print("Suma:" + str(numero1) + "+" + str(numero2) + "=" + str(suma(numero1,numero2)))
        elif operacion == "2":
            print("Resta:"+ str(numero1) + "-" + str(numero2) + "=" + str(resta(numero1,numero2)))
        elif operacion == "3":
            print("Multiplicación:"+ str(numero1) + "x" + str(numero2) + "=" + str(multiplicacion(numero1,numero2)))
        elif operacion == "4" and numero2 !=0:
            print("División:"+ str(numero1) + "/" + str(numero2) + "=" + str(division(numero1,numero2)))
        elif operacion == "4" and numero2 ==0:
            print("No se puede dividir por 0")
        else:
            print("Operación no programada en la calculadora")
        otra=input("Otra operacion?(s/n)")
    
