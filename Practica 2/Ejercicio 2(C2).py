def area_circulo (radio):
    """ float --> float
    OBJ: Calcular el area del circulo
    PRE: radio > 0 """
    from math import pi
    return pi*(radio**2)
#PRUEBA
#print ("Calcula el area de un circulo con radio = 10: ", area_circulo (10))

def area_cuadrado (lado_cuadrado):
    """ float --> float
    OBJ: Calcular el area del cuadrado
    PRE: lado > 0"""
    return lado_cuadrado**2
#PRUEBA
#print ("Calcula el area de un cuadrado con lado = 10: ", area_cuadrado(10))

def area_triangulo (base,altura):
    """float, float --> float
    OBJ: Calcular el area del triangulo
    PRE : base >= 0 y altura >=0"""
    return (base*altura)/2
#PRUEBA
#print ("Calcula el area de un triangulo con base = 10 y altura = 10: ", area_triangulo(10,10))

radio = float(input("Introduzca el radio del circulo: "))
while radio < 0:
    print ("El radio no puede ser negativo, vuelva a introducirlo porfavor.")
    radio = float(input(""))
print ()

lado = float(input("Introduzca el lado del cuadrado: "))
while lado < 0:
    print ("El lado no puede ser negativo, vuelva a introducirlo porfavor.")
    lado = float(input(""))
print ()

base = float(input("Introduzca la base del triangulo: "))
while base < 0:
    print ("La base no puede ser negativo, vuelva a introducirlo porfavor.")
    base = float(input(""))
print ()

altura = float(input("Introduzca la altura del triangulo: "))
while lado < 0:
    print ("La altura no puede ser negativo, vuelva a introducirlo porfavor.")
    altura = float(input(""))
print ()

print ("El area del circulo es: ", area_circulo(radio))
print ()
print ("El area del cuadrado es: ", area_cuadrado(lado))
print ()
print ("El area del triangulo es: ", area_triangulo(base, altura))
print ()
