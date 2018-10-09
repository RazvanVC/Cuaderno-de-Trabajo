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
    return entero

numero = leer_entero_valido_positivo ()
print (type(numero))

