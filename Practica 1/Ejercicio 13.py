print ("13. El salario base de un vendedor es de 2.000 euros mensuales. \n\
A este salario se le suma un 3% de comisión sobre el total de las ventas que ha \n\
realizado, pero al total obtenido hay que descontarle un 32% del IRPF. Escribe \n\
un programa que lea el importe de las ventas que ha realizado el venderdor \n\
durante el último mes y escriba el salario neto que cobrará ese mes.")
print ()

SalarioB = 2000

Ventas = float(input("¿Cuanto ha vendido este mes?"))
while Ventas < 0:
    print ("Las ventas no pueden ser negativas. \n\
Porfavor introduzca un valor positivo.")
    Ventas = float(input(""))
print ()
Comision = (Ventas*0.03)*0.68
SueldoNeto = SalarioB+Comision
print ("El vendedor cobraria: ", SueldoNeto, "euros.")
