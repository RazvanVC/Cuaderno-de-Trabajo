def tabla_multiplicar_de_un_numero (numero):
    """ int --> int
    OBJ: Tabla de multiplicar"""
    t = (numero*1,numero*2,numero*3,numero*4,numero*5,numero*6,numero*7,numero*8,numero*9,numero*10)
    return t

numero = int(input("¿Que tabla de multiplicar quieres saber?"))
Resultados = tabla_multiplicar_de_un_numero (numero)
print ()
print (numero, "x 1 = ",Resultados[0])
print ()
print (numero, "x 2 = ",Resultados[1])
print ()
print (numero, "x 3 = ",Resultados[2])
print ()
print (numero, "x 4 = ",Resultados[3])
print ()
print (numero, "x 5 = ",Resultados[4])
print ()
print (numero, "x 6 = ",Resultados[5])
print ()
print (numero, "x 7 = ",Resultados[6])
print ()
print (numero, "x 8 = ",Resultados[7])
print ()
print (numero, "x 9 = ",Resultados[8])
print ()
print (numero, "x 10 = ",Resultados[9])
