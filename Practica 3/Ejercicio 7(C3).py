def CalificacionesABCDEF(nota):
    if nota>=8.5:
        return "A"
    elif nota>=6.5:
        return "B"
    elif nota>=5:
        return "C"
    elif nota>=3.5:
        return "D"
    elif nota<3.5:
        return "F"
nota = float(input("Introduzca la nota"))
print ()
try:
    nota > 0
    nota < 10
    pass
except: 
    
    
print ()
print (CalificacionesABCDEF(nota))
