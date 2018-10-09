def leer_entero_valido ():
    """ nada --> int
        OBJ: Solicitar un entero al usuario, validarlo y retornarlo cuando \n\
        se asegura de que es un entero"""
    entero = input("Introduce un entero: ")
    print ()
    while type(entero) != int:
        try:
            entero = int(entero)
        except:
            print ("ERROR: No es un entero")
            print ()
            entero = input("Introduce un entero: ")
            print ()
        
    return entero

numero = leer_entero_valido ()

print (numero)
