PINTA = 473.176473 #mL
def mL_a_Pintas (mL):
    """ float --> float
    OBJ: Transforma los mililitros dados a pintas
    PRE: mL >= 0 """
    return (mL/PINTA)

#PRUEBA
#print ("Para 200 mL, el programa devuelve ", mL_a_Pintas (200), "pintas")
print ("Conversor de mL a pintas")
mL = float(input("¿Cuantos mL quieres convertir?"))
while mL < 0:
    print ("Los mL no pueden ser negativos. \n\
    Porfavor introduzca un valor positivo")
    mL = float(input(""))
print (mL, "mililitros equivalen a : ", mL_a_Pintas (mL), "pintas")
