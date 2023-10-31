numero1 = input("numero1?")
numero2 = input("numero2?")
numero1= int(numero1)    
numero2= int(numero2)
suma= numero1+numero2
resta= numero1-numero2
multiplicacion= numero1*numero2
if (numero2 == 0):
    print("No se puede dividir por 0")
else: 
    division= numero1/numero2

print("Operaciones básicas:" + "\n" +
      "Suma:" + str(numero1) + "+" + str(numero2) + "=" + str(suma) + "\n" +
      "Resta:"+ str(numero1) + "-" + str(numero2) + "=" + str(resta) + "\n" + 
      "Multiplicación:"+ str(numero1) + "x" + str(numero2) + "=" + str(multiplicacion) + "\n" + 
      "División:"+ str(numero1) + "/" + str(numero2) + "=" + str(division)
)
