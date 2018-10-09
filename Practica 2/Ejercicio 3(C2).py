EQUIVALENCIA = 10**28

def metros_cuadrados_a_Barn (m2):
    """ float --> float
    OBJ: Pasar de metros cuadrados a Barn
    PRE: metros cuadrados >= 0 """
    return m2 /(EQUIVALENCIA)
def Barn_a_metros_cuadrados (Barns):
    """ float --> float
    OBJ: Pasar de Barn a metros cuadrados
    PRE: Barn >= 0 """
    return Barns * (EQUIVALENCIA)

print ("Conversor de metros cuadrados a Barn")
Metros_cuadrados = float(input("¿Cuantos metros cuadrados quieres convertir?"))
print ()
while Metros_cuadrados < 0:
    print ("Los metros cuadrados no pueden ser negativos. \n\
Porfavor introduzca un valor positivo")
    Metros_cuadrados = float(input(""))
print ()
print (Metros_cuadrados, "metros cuadrados son : ", metros_cuadrados_a_Barn (Metros_cuadrados), "Barn")
print ()
print ("Conversor de Barn a metros cuadrados")
Barn = float(input("¿Cuantos Barn quieres convertir?"))
while Barn < 0:
    print ("Los Barn no pueden ser negativos. \n\
Porfavor introduzca un valor positivo")
    Barn = float(input(""))
print (Barn, "Barn son : ", Barn_a_metros_cuadrados (Barn), "metros cuadrados")
