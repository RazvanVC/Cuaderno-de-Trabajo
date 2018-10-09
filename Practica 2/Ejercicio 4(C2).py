def media (num1, num2, num3):
    """ float, float, float --> float
    OBJ: Calcular la media aritmetica de 3 notas
    PRE: num > 0 """
    return (num1 + num2 + num3)/3
#PRUEBA
#print ("Calcula la media de 2, 4, 10. \nMedia = ",  media (2, 4, 10))

nota1 = float(input("Introduzca la nota 1: "))
while nota1 < 0:
    print ("La nota ha de ser mayor que 0. \nPorfavor vuelva a introducirla")
    nota1 = float(input(""))
print ()
nota2 = float(input("Introduzca la nota 2: "))
while nota2 < 0:
    print ("La nota ha de ser mayor que 0. \nPorfavor vuelva a introducirla")
    nota2 = float(input(""))
print ()
nota3 = float(input("Introduzca la nota 3: "))
while nota3 < 0:
    print ("La nota ha de ser mayor que 0. \nPorfavor vuelva a introducirla")
    nota3 = float(input(""))
print ()
print ("La nota media es: ", media (nota1,nota2,nota3))

