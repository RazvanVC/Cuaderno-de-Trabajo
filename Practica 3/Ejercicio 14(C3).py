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

##PRUEBA:
##numero = leer_entero_valido ()
##print (numero)

numero = 0
contadorpositivo = 0
contadornegativo = 0
contadorceros = 0
while numero != -9999:
    numero = leer_entero_valido ()
    if numero < 0:
        contadornegativo = contadornegativo + 1
    elif numero > 0:
        contadorpositivo = contadorpositivo + 1
    else:
        contadorceros = contadorceros + 1
        
contadortotal = contadorpositivo + contadorceros + contadornegativo

print ("¡¡Has acertado!! El numero era -9999.")
print ("Has usado: ", contadortotal, "intentos. De los cuales; \n",">",contadorpositivo,"han sido positivos \n",
        ">", contadornegativo,"han sido negativos.")
