def Distancia (x1,y1,z1,x2,y2,z2):
    from math import sqrt
    distancia = sqrt(pow((x2-x1),2)+pow((y2-y1),2)+pow((z2-z1),2))
    return distancia

print (Distancia (0,2,0,7,2,-1))
