print ("5. Escribe un programa que dada una hora (expresada en hora, minutos y \n\
segundos) muestre por pantalla el total de segundos transcurridos desde la\n\
última medianoche y los que quedan para la siguiente medianoche")
print ()
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
HoraDiaTotal = 86400
SegundoActual = (Hora*3600 + Minuto*60 + Segundo)
SegundoMid = HoraDiaTotal - SegundoActual

print ("Faltan :", SegundoMid, "para la proxima medianoche")
print ()
print ()
print ("Han pasado :", SegundoActual, "desde la ultima medianoche")

