print ("6. Una industria mantiene una flota de camiones para repartir productos.\n\
En cada viaje, el conductor anota la distancia recorrida en kilómetros,\n\
los litros de gasoil utilizados, el coste del gasoil y los demás costes de \n\
mantenimiento del camión. Como parte del proceso de contabilidad, el controlador necesita \n\
calcular, para cada camión y para cada viaje, los kilómetros recorridos \n\
por litro, el coste total del viaje y el coste por kilómetro. Diseña un programa  \n\
sencillo que lleve a cabo estos cálculos para un camión en un viaje.")

KM = float(input("¿Cuantos kilometros has echo?"))
while KM < 0:
    print ("Los kilometros no pueden ser negativos. \n\
Porfavor uelva a introducir el numero de kilometros.")
    KM = float(input(""))
    
print ()
Gasolina = float(input("¿Cuanta gasolina has consumido?"))
while Gasolina < 0:
    print ("Los litros de gasolina no pueden ser negativas. \n\
Porfavor vuelva a introducir los litros de gasolina.")
    Gasolina = float(input(""))

print ()
CosteGasolina = float(input("¿Cuanto cuesta el litro de gasolina?"))
while CosteGasolina < 0.1:
    print ("El coste de la gasolina no puede ser negativo. \n\
Porfavor vuelva a introducir el coste de la gasolina.")
    CosteGasolina = float(input(""))

print ()
CMantenimiento = float(input("¿Cual ha sido el coste de mantenimiento?"))
while CMantenimiento < 0:
    print ("El coste de mantenimiento no puede ser negativo. \n\
Porfavor vuelva a introducir el coste de mantenimiento.")
    CMantenimiento = float(input(""))
print ()
KMLitro = KM / Gasolina
CosteT = Gasolina*CosteGasolina + CMantenimiento
CosteKM = CosteT/KM

print ()
print ()
print ("Tus Datos son: ")
print ("Kilometros recorrido: ", KM, "Kilómetros")
print ("Litros gasoil usados: ", Gasolina, "Litros")
print ("EL litro de gasoil está a: ", CosteGasolina, "€/Litro")
print ("El mantenimiento ha sido: ", CMantenimiento, "€")
print ("Ha recorrido: ", KMLitro, "kilometros por cada litro de gasolina")
print ("El coste total del viaje ha sido: ", CosteT, "€")
print ("El coste por kilometro ha sido: ", CosteKM, "€")


