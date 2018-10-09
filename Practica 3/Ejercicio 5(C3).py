def validar_real (numero):
    try:
        dato = float(numero)
        return True
    except:
        return False
        


print (validar_real(25))
