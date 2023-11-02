numero1=0
numero2=1
def suma(numero1,numero2):
    return numero1+numero2
def resta(numero1,numero2):
    return numero1-numero2
def multiplicacion(numero1,numero2):
    return numero1*numero2
def division(numero1,numero2):
    if (numero2 == 0):
        return print("No se puede dividir por 0")
    else: 
        return numero1/numero2
#Esto es para evitar fallos en los ejercicios siguientes al importar
if __name__ == "__main__":
    numero1 = input("numero1?")
    numero2 = input("numero2?")
    numero1= int(numero1)    
    numero2= int(numero2)
    print("Operaciones básicas:" + "\n" +
      "Suma:" + str(numero1) + "+" + str(numero2) + "=" + str(suma(numero1,numero2)) + "\n" +
      "Resta:"+ str(numero1) + "-" + str(numero2) + "=" + str(resta(numero1,numero2)) + "\n" + 
      "Multiplicación:"+ str(numero1) + "x" + str(numero2) + "=" + str(multiplicacion(numero1,numero2)) + "\n" + 
      "División:"+ str(numero1) + "/" + str(numero2) + "=" + str(division(numero1,numero2))
    )
