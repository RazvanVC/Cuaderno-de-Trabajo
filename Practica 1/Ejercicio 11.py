print ("11. La temperatura expresada en grados centígrados TC, se puede convertir \n\
a grados Fahrenheit (TF) mediante la siguiente fórmula: TF = 9*TC/5 + 32. \n\
Escribe un programa que pida al usuario la temperatura en grados Fahrenheit \n\
y devuelva la temperatura en grados Centígrados.")
print ()

GradosF = float(input("¿Cual es la temperatura en Fahrenheit?"))
print ()

GradosC = (37*GradosF)/9

print ("Hacen :", GradosC, "grados Centigrados")
