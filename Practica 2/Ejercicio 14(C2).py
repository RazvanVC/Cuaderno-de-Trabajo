def sumarcomplejos (a,b,c,d):
    """float,float,float,float --> float,complex
    OBJ: Hacer la suma de un numero real mas uno complejo."""
    return complex ((a+c),(b+d))
def restarcomplejos (a,b,c,d):
    """float,float,float,float --> float,complex
    OBJ: Hacer la resta de un numero real menos uno complejo."""
    return complex ((a-c),(b-d))
def multiplicarcomplejos (a,b,c,d):
    """float,float,float,float --> float,complex
    OBJ: Hacer la multiplicacion de un numero real por uno complejo."""
    return complex ((a*c - b*d),(a*d+b*c))
def dividircomplejos (a,b,c,d):
    """float,float,float,float --> float,complex
    OBJ: Hacer la division de un numero real entre uno complejo."""
    return complex (((a*c+b*d)/(pow(c,2) + pow(d,2))),((b*c-a*d)/(pow(c,2)+pow(d,2))))


print ("Pruebas: ")
print ("Suma de Numeros Complejos, siendo a=7; b=2; c=3; d=4.\n\
La suma da: ",sumarcomplejos(7,2,3,4))
print ()
print ("Resta de Numeros Complejos, siendo a=1; b=4; c=2; d=5. \n\
La resta da: ",restarcomplejos(1,4,2,5))
print()
print ("Multiplicacion de Numeros Complejos, siendo a=1; b=4; c=7; d=2. \n\
La multiplicacion da: ",multiplicarcomplejos(1,4,7,2))
print ()
print ("Division Numeros Complejos, siendo a=4; b=3, c=2, d=1. \n\
La division da: ",dividircomplejos(4,3,2,1))


