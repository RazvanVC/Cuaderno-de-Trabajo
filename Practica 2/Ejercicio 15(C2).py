def EsBisiesto (anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False

anio = int(input("Introduzca el año: "))
Bisisesto = EsBisiesto(anio)
print ()
if Bisisesto == True:
    print ("Su año,",anio,"es bisiesto")
else:
    print ("Su año,",anio,"no es bisiesto")
