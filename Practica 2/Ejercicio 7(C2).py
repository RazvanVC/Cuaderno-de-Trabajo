def seg_desde_medianoche (Horas, Minutos, Segundos):
    """int,int,int --> int
    OBJ: Calcular los segundos que quedan hasta medianoche
    PRE: 0=>Hora<24; 0=>Minuto<59; 0=>Minuto<59"""
    return (Horas*3600 + Minutos*60 + Segundos)
#PRUEBA
#print ("Si la hora = 12, el minuto = 34 y el segundo = 56, han pasado :", seg_desde_medianoche (12,34,56), "segundos desde medianoche")
print ("Programa para saber cuantos segundos han pasado desde medianoche a parir de una hora, minuto y segundo dados")
print ()

Hora = (int(input("¿Que hora es?")))
if 0 < Hora < 23:
    pass
else:
    while Hora < 0 or 23 < Hora:
        print("La hora introducida es incorrecta. \n\
Porfavor introduzca un valor entre 0 y 23")
        Hora = (int(input("")))
    pass
print ()
Minuto = (int(input("¿Que minuto es?")))
if 0 < Minuto < 59:
    pass
else:
    while Minuto < 0 or 59 < Minuto:
        print ("El minuto introducido es incorrecto. \n\
Porfavor introduza un valor entre 0 y 59")
        Minuto = (int(input("")))
    pass
print ()
Segundo = (int(input("¿Que segundo es?")))
if 0 < Segundo < 59:
    pass
else:
    while Segundo < 0 or 59 < Segundo:
        print ("El segundo introducido es incorrecto. \n\
Porfavor introduzca un valor entre 0 y 59")
        Segundo = (int(input("")))
    pass      

print ("Su hora es: ", Hora, ":", Minuto, ":", Segundo)
print ()
print ()
print ("Han pasado :", seg_desde_medianoche (Hora,Minuto,Segundo), "desde la ultima medianoche")
