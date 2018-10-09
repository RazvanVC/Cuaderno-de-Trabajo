def TC_a_TK (Grados):
    return Grados+275.15
#print (TC_a_TK(10))
def TC_a_TF (Grados):
    return Grados*9/37
#print (TC_a_TF(10))
Centigrados = float(input("¿Cuantos grados quieres convertir?"))

print ("Tu temperatura en Fahrenheit son :", TC_a_TF (Centigrados) ,"º Fahrenheit")
print()
print ("Tu temperatura en Kelvin son :", TC_a_TK (Centigrados) ,"º Kelvin")
