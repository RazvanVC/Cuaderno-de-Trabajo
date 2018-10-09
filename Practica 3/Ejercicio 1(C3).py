def dtocontado (precio):
    """ """
    if precio > 100:
        return precio*0.95
    else:
        return precio
def dtotarjeta (precio):
    """ """
    if precio > 100:
        return precio*0.98
    else:
        return precio

        

preciocompra = input("¿Cual ha sido el importe de la compra?")
print ()
try:
    preciocompra = float(preciocompra)
except:
    print ("Algo ha fallado: no es posible calcular el descuento")


while preciocompra < 0:
    print ("Algo ha fallado: el importe no puede ser negativo")
    print ()
    preciocompra = float(input("¿Cual ha sido el importe de la compra?"))

tipopago= input("¿Como va a pagar Efectivo o Tarjeta? ")
if tipopago == "Efectivo":
    print ("El precio de su compra es :", round(dtocontado(preciocompra),2))
elif tipopago == "Tarjeta":
    print ("El precio de su compra es :", round(dtotarjeta(preciocompra),2))

