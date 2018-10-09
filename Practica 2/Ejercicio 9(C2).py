def comprobar_dos_coordenadas_dentro_de_una_funcion_Predeterminada (x,y):
    """float,float-->T/F
    OBJ: Ccomporbar dos valores dentro de esta funcion x2+y2=1000"""
    from math import sqrt
    return round(x**2+y**2) == 1000
#PRUEBA
#print ("Con los valores x=31.62 e y=0 comprueba si esas coordenadas estan dentro de la funcion: ", comprobar_dos_coordenadas_dentro_de_una_funcion_Predeterminada (31.62,0))

Coordenada1 = float(input("Inserte la coordenada X: "))
print ()
Coordenada2 = float(input("Inserte la coordenada Y: "))
print ()
Condicion = comprobar_dos_coordenadas_dentro_de_una_funcion_Predeterminada (Coordenada1, Coordenada2)
if Condicion == True:
    print ("Las coordenadas X=",Coordenada1,"e Y=",Coordenada2,"si se encuentran dentro de la funcion.")
else :
    print ("Las coordenadas X=",Coordenada1,"e Y=",Coordenada2,"no se encuentran dentro de la funcion.")
