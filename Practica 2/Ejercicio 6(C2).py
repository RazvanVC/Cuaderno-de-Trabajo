def radianes_a_grados (radianes):
    """float --> float
    OBJ: Cambiar de radianes a grados"""
    from math import degrees
    return degrees (radianes)

#PRUEBA
#print ("Con la variable radianes = 2, la funcion devuelve: ", radianes_a_grados (-2), "Grados")

radianes = float(input("¿Cuantos radianes quieres convertir?"))
print ()
print (radianes, "radianes convertidos a grados son: ", radianes_a_grados (radianes), "Grados")

    
