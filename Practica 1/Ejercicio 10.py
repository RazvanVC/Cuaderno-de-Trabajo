print ("Escribe un programa que, a partir de 3 números reales, calcule su media,\n\
       suma total y producto total y muestre todos estos da")
print ()

Num1 = float(input("¿Cual es el numero 1?"))
Num2 = float(input("¿Cual es el numero 2?"))
Num3 = float(input("¿Cual es el numero 3?"))

print ()

SumaTot = Num1 + Num2 + Num3
Media = (SumaTot)/3
ProducTot = Num1*Num2*Num3

print ("Tu media es: ", Media)
print ()
print ("La suma total es: ", SumaTot)
print ()
print ("El producto total es: ", ProducTot)
