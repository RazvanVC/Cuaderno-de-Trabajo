print ("Escribe un programa que lea los lados de un rectángulo, calcule su \n\
       área y perímetro y los muestre por pantalla.")
print ()
unidad = input("¿En que medida vas a introducir los datos?")
lado1= float(input("¿Cuanto mide el lado 1?"))
while lado1 < 0:
    print ("El lado no puede tener un valor negativo. \n\
Porfavor introduzca de nuevo el valor.")
    lado1= float(input(""))
print ()
lado2= float(input("¿Cuanto mide el lado 2?"))
while lado2 < 0:
    print ("El lado no puede tener un valor negativo. \n\
Porfavor introduzca de nuevo el valor.")
    lado2= float(input(""))

Area=lado1*lado2

print("Tu area es: ", Area, unidad)
