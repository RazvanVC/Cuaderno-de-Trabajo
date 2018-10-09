def comprobar_un_numero_dentro_de_una_funcion_Cualquiera(x,ndex,y,ndey,igualdad):
    return round(x**ndex + y**ndey) == igualdad
#PRUEBA
#print ("Comprueba para x=12, con el exponente elevado a a la 13, \n\
#e y=2 con el exponente elevado a 3, si dichos valores concuerdan \n\
#con el resultado 2341\n",comprobar_un_numero_dentro_de_una_funcion_Cualquiera (12,13,2,3,2341))

print ("Programa para comprobar unos valores dentro de una funcion cualquiera")
print ()
Coordenada1 = float(input("Inserte la coordenada X: "))
print ()
Exponente_de_X = float(input("Inserte el exponente de X: "))
print ()
Coordenada2 = float(input("Inserte la coordenada Y: "))
print ()
Exponente_de_Y = float(input("Inserte el exponente de Y: "))
print ()
Resultado = float(input("Inserte el resultado de la funcion: "))

Condicion = comprobar_un_numero_dentro_de_una_funcion_Cualquiera (Coordenada1,Exponente_de_X,Coordenada2,Exponente_de_Y,Resultado)
if Condicion == True:
    print ("Las coordenadas X=",Coordenada1,"e Y=",Coordenada2,"si se encuentran dentro de la funcion.")
else :
    print ("Las coordenadas X=",Coordenada1,"e Y=",Coordenada2,"no se encuentran dentro de la funcion.")

