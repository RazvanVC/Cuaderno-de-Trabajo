print ("14. Se desea conocer el importe en Libras Esterlinas (GBP) al cambio \n\
de una cantidad en Euros (EUR). Escribe un programa que, a partir de una cierta \n\
cantidad en euros y del tipo de cambio del día, muestre el equivalente en libras\n\
teniendo en cuenta que la casa de cambio retiene una comisión del 2% sobre el\n\
total de la operación.")
print()
Euros = float(input("¿Cuanto Euros quieres cambiar?"))
while Euros < 0:
    print ("El valor no puede ser negativo. \n\
Porfavor introduzca un nuevo valor positivo")
    Euros = float(input(""))
print ()
Cambio = float(input("¿Cual es el tipo de cambio?"))
while Cambio < 0:
    print ("El valor no puede ser negativo. \n\
Porfavor introduzca un nuevo valor positivo")
    Cambio = float(input(""))
print()
Libras = (Euros*Cambio)*0.98

print ("Obtendrias: ", Libras, "Libras Esterlinas")
