#Constantes comprobación microempresa
min_empleados = 10
min_facturacion = 2 #MEuros
min_balance = 2 #MEuros
print ("Datos para ser Microempresa")
print ("Empleados", min_empleados)
print ("Facturacion", min_facturacion)
print ("Balance", min_balance)
print ()

#Constantes de la empresas
empleados = 20
facturacion = 18 #MEuros
balance = 5 #MEuros
print ("Datos Empresa")
print ("Empleados", empleados)
print ("Facturacion", facturacion)
print ("Balance", balance)
print ()

es_micro = empleados<min_empleados and facturacion<min_facturacion or balance<min_balance

if es_micro:
    print("Es una microempresa")
else:
    print("No es una microempresa")
