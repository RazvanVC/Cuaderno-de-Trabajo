def conteo_serie_armonica(numero):
    """ int --> int
    OBJ: Contar los numeros que hacen falta para superar el numero introducido mediante la serie armonica
    PRE: Los numeros a partir del 19 tardan en procesarse"""
    if numero >= 1:
        suma = 0
        determinante = 1
        conteo = 0
        while suma <= numero:
            suma = suma + 1/determinante
            determinante = determinante + 1
            conteo = conteo + 1
        return conteo

##print (conteo_serie_armonica(5))

def leer_entero_valido_positivo ():
    """ nada --> int
        OBJ: Solicitar un entero positivo al usuario, validarlo y retornarlo cuando \n\
        se asegura de que es un entero"""
    entero = input("Introduce un entero positivo: ")
    print ()
    Condicion = False
    while Condicion != True: 
        while int(entero) < 0:
            print ("ERROR: No es un entero positivo.")
            entero = input("Introduce un entero positivo: ")
            try:
                entero = int(entero)
            except:
                while type(entero) != int:
                    try:
                        entero = int(entero)
                    except:
                        print ("ERROR: No es un entero.")
                        print ()
                        entero = input("Introduce un entero positivo: ")
                        print ()

        Condicion = True
    return int(entero)


##numero = leer_entero_valido_positivo ()
##print (numero)

Numero = leer_entero_valido_positivo ()
print ("Para tu", Numero, "hacen falta",conteo_serie_armonica(Numero), "numeros de la serie armonica") 
