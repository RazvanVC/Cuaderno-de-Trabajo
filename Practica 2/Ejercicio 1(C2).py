def fuerza (masa, aceleracion):
    """ float, float, --> float
    OBJ: Calcular la fuerza mediante la masa y la aceleracion
    PRE: masa > 0 y aceleracion > 0"""
    return masa*aceleracion

print ("Calcular la fuera a partir de la masa y la aceleracion")
masa = float(input("¿Cual es la masa?"))
while masa <= 0:
    print("La masa no puede ser negativa. \n\
    Vuelva a inroducir la masa porfavor.")
    masa = float(input(""))
print ()
aceleracion = float(input("¿Cual es la aceleracion?"))
while aceleracion <= 0:
    print("La aceleracion no puede ser negativa. \n\
    Vuelva a inroducir la aceleracion porfavor.")
    aceleracion = float(input(""))
print ()

print ("La fuerza es : ", fuerza (masa,aceleracion))
