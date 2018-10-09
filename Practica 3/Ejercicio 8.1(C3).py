def ordenarnums (num1,num2,num3):
    """float,float,float --> tuple
    OBJ: Ordenar 3 numeros de menor a mayor. """
    if num1 <= num2 and num2 <= num3:
        t = [num1,num2,num3]
    elif num1 <= num3 and num3 <= num2:
        t = [num1,num3,num2]
    elif num2 <= num1 and num1 <= num3:
        t = [num2,num1,num3]
    elif num2 <= num3 and num3 <= num1:
        t = [num2,num3,num1]
    elif num3 <= num1 and num1 <= num2:
        t = [num3,num1,num2]
    elif num3 <= num2 and num2 <= num1:
        t = [num3,num2,num1]    
    return t
#PRUEBAS
##print ("ordenarnums(3,6,12)",ordenarnums(3,6,12)) #Working...
##print ("ordenarnums(3,17,7)",ordenarnums(3,17,7)) #Working...
##print ("ordenarnums(14,6,18)",ordenarnums(14,6,18)) #Working...
##print ("ordenarnums(17,7,12)",ordenarnums(17,7,12)) #Working...
##print ("ordenarnums(14,23,2)",ordenarnums(14,23,2))
##print ("ordenarnums(28,19,9)",ordenarnums(28,19,9))

#COMPROBADORES
try:
    numero1 = float(input("Introduzca un numero: "))
    numero2 = float(input("introduzca otro numero: "))
    numero3 = float(input("introduzca otro numero: "))
except:
    print ("ERROR: El valor introducido no es un numero o has introducido dos valores idénticos")
#PANTALLA
else:
    print ("Tus numeros son: ", numero1, ",", numero2, "y", numero3, ".")
    print ()
    print ("Tus numeros ordenados de menor a mayor serian: ", ordenarnums(numero1,numero2,numero3))



