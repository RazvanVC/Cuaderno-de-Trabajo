def ordenarnums (num1,num2,num3):
    """float,float,float --> tuple
    OBJ: Ordenar 3 numeros de menor a mayor. """

    if num1 > num2 and num1 > num3:
        if num2 > num3:
            t = [num3,num2,num1]
        elif:
            t = [num2,num3,num1]
        else:
            pass
    elif num1 > num2 and num1 < num3:
        if num2 > num3:
            t = [num3,num1,num2]
        else:
            t = [num2,num1,num3]
    elif num1 < num2 and num1 < num3:
        if num2 > num3:
            t = [num1,num3,num2]
        else:
            t = [num1,num2,num3]
    return t
#PRUEBAS
#print ("ordenarnums(12,6,3)",ordenarnums(12,6,3))
#print ("ordenarnums(17,3,7)",ordenarnums(17,3,7))
#print ("ordenarnums(5,8,6)",ordenarnums(5,8,4))
#print ("ordenarnums(12,7,17)",ordenarnums(12,7,17))
#print ("ordenarnums(2,23,14)",ordenarnums(2,23,14))
#print ("ordenarnums(7,14,18)",ordenarnums(7,14,18))
#COMPROBADORES
try:
    numero1 = float(input("Introduzca un numero"))
    numero2 = float(input("introduzca un numero"))
    numero3 = float(input("introduzca un numero"))
except:
    print ("ERROR: El valor introducido no es un numero")
#PANTALLA
else:
    print ("Los numeros ordenadores serian: ", ordenarnums(numero1,numero2,numero3))
