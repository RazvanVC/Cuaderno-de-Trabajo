def TC_a_TF (Grados):
    """float --> float
    OBJ: Pasar de Centigrados a Fahrenheit""""
    return 9*Grados
def TC_a_TK (Centigrados):
    """float --> float
    OBJ: Pasar de Centigrados a Kelvin""""
    return Centigrados+273.15

Centigrados = float(input("¿Cuantos grados quieres convertir?"))

print ("Tu temperatura en Fahrenheit son :",TC_a_TF(Centigrados),"º Fahrenheit")
print()
print ("Tu temperatura en Kelvin son :",TC_a_TK(Centigrados),"º Kelvin")
