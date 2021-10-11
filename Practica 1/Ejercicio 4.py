print ("4. Escribe un programa en Python que calcule el impuesto que debe pagar un contribuyente a partir de sus ingresos anuales y el número de hijos. \n\
El impuesto a pagar es un tercio del ingreso imponible, siendo este último igual a los ingresos totales menos una deducción personal de 600€ y otra \n\
deducción de 60€ por hijo.")
print () 

ingresos_anuales = (float(input("¿Cuales son los ingresos anuales?")))
print ("Ingresos Anuales: ", ingresos_anuales)
num_hijos = (int(input("¿Cuantos hijos tienes?")))
print ("Número hijos: ", num_hijos)
imp_imponible = ingresos_anuales-(600+(60*num_hijos))
imp_pagar = imp_imponible/3
print ("Impuesto a pagar: ", imp_pagar)