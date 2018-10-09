def KM_a_HM (KM):
    """float --> float
    OBJ: Cambiar de KM a HM
    PRE: KM>0"""
    return KM*10
#PRUEBA
#print ("Para 10 KM la funcion devuelve: ", KM_a_HM (10), "Hm")
def KM_a_DM (KM):
    """float --> float
    OBJ: Cambiar de KM a DM
    PRE: KM>0"""
    return KM*100
#PRUEBA
#print ("Para 10 KM la funcion devuelve: ", KM_a_DM (10), "Dm")
def KM_a_M (KM):
    """float --> float
    OBJ: Cambiar de KM a M
    PRE: KM>0"""
    return KM*1000
#PRUEBA
#print ("Para 10 KM la funcion devuelve: ", KM_a_M (10), "m")

KM = float(input("¿Cuantos kilometros quieres convertir?"))
print ()

print ("Resultado en Hm: ", KM_a_HM (KM), "Hm")
print ()
print ("Resultado en Dm: ", KM_a_DM (KM), "Dm")
print ()
print ("Resultado en  m: ", KM_a_M (KM), "m")
