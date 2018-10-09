def validar_entero (numero):
    try:
        dato = int(numero)
        return True
    except:
        return False
        


print (validar_entero("Hola"))
