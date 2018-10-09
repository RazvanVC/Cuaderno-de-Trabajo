print ("5. La Tasa de Interés Efectivo Anual (TIEA) se calcula a partir de una \n\
tasa nominal anual (TNA) y de un determinado número entero de períodos de \n\
capitalización (m)de la tasa nominal anual en el año: TIEA=(1 + TNA/m)^n-1, \n\
siendo n el número de periodos total de un año, es decir, 12 si hablamos de \n\
períodos mensuales. Escribe una función que calcule el TIEA a partir del TNA \n\
y el número de períodos (4 si es trimestral, 2 si es semestral, etc.).")
print ()

N_PERIODOS = 12 #Constante

def tiea (tna, periodo_cap):
    """int, int --> float
    OBJ: Calcular la Tasa de Interes Efectuvo Anual (TIEA)
    PRE: tna > 0 y periodo_cap > 0 y periodo_cap < 12"""
    return ((1+(tna/periodo_cap))**N_PERIODOS-1)

#PRUEBA

TIEA = tiea (133,12)
print ("Para el TNA = 133 y el Periodo de Capitalizacion = 12. El TIEA es: ", TIEA)



periodo_cap = int(input("¿Cuales son los periodos de capitalizacion?")) #Variable m
while periodo_cap<=0 or 12<periodo_cap:
    print ("El periodo de capitalizacion no es correcto. \n\
Porfavor introduzca un numero entre 1 y 12")
    periodo_cap = int(input(""))
print ()

tna = int(input("¿Cual es el TNA?")) #Variable TNA
while tna < 0:
    print ("El TNA no puede ser negativo. \n\
Porfavor introduzca un valor positivo.")
    tna = int(input(""))
print ("El TIEA = ",tiea (tna,periodo_cap))
